from django.shortcuts import render, redirect, get_object_or_404
from .models import Projet
from .forms import ProjetForm
from batiment.models import Batiment
from calorifu.models import Calorifu
from django.db.models.functions import Coalesce
from django.db.models import Sum, F, Value, DecimalField, IntegerField, Q, FloatField
from collections import defaultdict
from decimal import Decimal

# Liste des projets
def projet_list(request):
    projets=Projet.objects.all()
    return render(request,'projet/list.html',{'projets':projets})

def to_decimal(val):
    """Convertit float/int/None en Decimal en toute sécurité"""
    return Decimal(str(val or 0))


def articles_par_systeme(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    systemes = projet.systemes.prefetch_related('systeme_articles__equipement')

    systemes_data = []

    for systeme in systemes:
        articles = []
        total_systeme = Decimal('0')
        for article in systeme.systeme_articles.all():
            montant = (article.qte or Decimal('0')) * (article.equipement.prix or Decimal('0'))
            total_systeme += montant
            articles.append({'article': article, 'montant': montant})

        systemes_data.append({
            'systeme': systeme,
            'articles': articles,
            'total': total_systeme
        })

    context = {
        'projet': projet,
        'systemes_data': systemes_data,
    }
    return render(request, 'projet/articles_par_systeme.html', context)


def articles_global(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    articles_groupes = defaultdict(lambda: {
        'nom': '',
        'unite': '',
        'prix': Decimal('0'),
        'qte_totale': Decimal('0'),
        'montant_total': Decimal('0'),
    })
    total_projet = Decimal('0')

    for systeme in projet.systemes.prefetch_related('systeme_articles__equipement'):
        for article in systeme.systeme_articles.all():
            montant = (article.qte or Decimal('0')) * (article.equipement.prix or Decimal('0'))
            total_projet += montant
            eq = article.equipement
            data = articles_groupes[eq.id]
            data['nom'] = eq.nom
            data['unite'] = eq.unite
            data['prix'] = eq.prix or Decimal('0')
            data['qte_totale'] += article.qte or Decimal('0')
            data['montant_total'] += montant

    context = {
        'projet': projet,
        'articles_groupes': articles_groupes.values(),
        'total_projet': total_projet,
    }
    return render(request, 'projet/articles_global.html', context)

def calorifugeage_par_systeme(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    systemes = projet.systemes.prefetch_related('systeme_calorifus')
    context = {
        'projet': projet,
        'systemes': systemes,
    }
    return render(request, 'projet/calorifugeage_par_systeme.html', context)


def calorifugeage_global(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    calorifus = Calorifu.objects.filter(systeme__projet=projet)

    totaux = defaultdict(lambda: Decimal('0'))
    for c in calorifus:
        totaux['tuy'] += c.tuy or Decimal('0')
        totaux['tuy_cds'] += c.tuy_cds or Decimal('0')
        totaux['tuy_emb'] += c.tuy_emb or Decimal('0')
        totaux['tuy_rob'] += c.tuy_rob or Decimal('0')
        totaux['isol_cds'] += c.isol_cds or Decimal('0')
        totaux['isol_emb'] += c.isol_emb or Decimal('0')
        totaux['isol_rob'] += c.isol_rob or Decimal('0')
        totaux['antifeu_cds'] += c.antifeu_cds or Decimal('0')
        totaux['antifeu_emb'] += c.antifeu_emb or Decimal('0')
        totaux['antifeu_rob'] += c.antifeu_rob or Decimal('0')

    context = {
        'projet': projet,
        'totaux': totaux,
    }
    return render(request, 'projet/calorifugeage_global.html', context)

def projet_batiments(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    batiments=projet.batiments_batiment.filter(pk=pk)
    return render(request,'projet/batiments.html',{'batiments':batiments,  'projet': projet})


#***********************************************************  CRUD **********************************************************/

def show(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    return render(request, 'projet/show.html', {'projet': projet})

# Ajouter un projet
def new(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projet_list')
    else:
        form = ProjetForm()
    return render(request, 'projet/new.html', {'form': form})

# Modifier un projet
def edit(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    if request.method == 'POST':
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('projet_edit', pk=projet.pk)
    else:
        form = ProjetForm(instance=projet)
    return render(request, 'projet/edit.html', {'form': form})

# Supprimer un projet
def delete(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    if request.method == 'POST':
        projet.delete()
        return redirect('projet_list')
    return render(request, 'projet/delete.html', {'projet': projet})

# Liste des projets
def projet_list(request):
    projets=Projet.objects.all()
    return render(request,'projet/list.html',{'projets':projets})
