from django.shortcuts import render, redirect, get_object_or_404
from .models import Projet
from .forms import ProjetForm
from article.models import Article
from django.db.models import Sum, F

# Liste des projets
def list(request):
    projets=Projet.objects.all()
    return render(request,'projet/list.html',{'projets':projets})


def show(request,pk):
    projet=get_object_or_404(Projet,pk=pk)
    articles_groupes = (
        Article.objects
        .filter(systemes_lies__projet=projet)
        .values('nom')  # group by nom
        .annotate(
            total_qte=Sum('qte'),
            total_montant=Sum(F('prix') * F('qte'))
        )
    )


    return render(request, "projet/show.html", {
        "projet": projet,
        "articles_groupes": articles_groupes,
    })


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
