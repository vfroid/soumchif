from django.shortcuts import render, redirect, get_object_or_404
from systeme.models import Systeme
from article.models import Article
from systeme.forms import SystemeForm, ArticleSystemeFormSet




#******************************************** CRUD *************************************************/
def list(request):
    systemes=Systeme.objects.all()
    return render(request,'systeme/list.html', {'systemes': systemes })

def show(request, pk):
    systeme = get_object_or_404(Systeme, pk=pk)

    # uniquement les articles liés
    articles = systeme.articles.all()

    # total (optionnel mais utile)
    total = sum(a.montant for a in articles)

    return render(request, "systeme/show.html", {
        "systeme": systeme,
        "articles": articles,
        "total":total,
    })



def new(request):
    if request.method == "POST":
        form = SystemeForm(request.POST)

        # ⚠️ récupérer le type AVANT validation
        type_id = request.POST.get('type')

        if type_id:
            articles_qs = Article.objects.filter(systeme_types__id=type_id).distinct()
        else:
            articles_qs = Article.objects.none()

        formset = ArticleSystemeFormSet(request.POST, queryset=articles_qs)

        if form.is_valid() and formset.is_valid():
            systeme = form.save()

            systeme.articles.clear()

            for f in formset:
                if f.cleaned_data.get('ajouter'):
                    article = f.instance
                    article.qte = f.cleaned_data.get('qte', 0)
                    article.prix = f.cleaned_data.get('prix', 0)
                    article.save()
                    systeme.articles.add(article)

            print(formset.errors)
            print([f.cleaned_data for f in formset])
            return redirect('systeme_list')

    else:
        form = SystemeForm()
        # 👉 afficher tous les articles au départ (plus simple)
        articles_qs = Article.objects.all()

        formset = ArticleSystemeFormSet(queryset=articles_qs)

    return render(request, "systeme/new.html", {
        "form": form,
        "formset": formset
    })



def edit(request, pk):
    systeme = get_object_or_404(Systeme, pk=pk)

    if request.method == "POST":
        form = SystemeForm(request.POST, instance=systeme)

        type_id = request.POST.get('type')

        if type_id:
            articles_qs = Article.objects.filter(systeme_types__id=type_id).distinct()
        else:
            articles_qs = Article.objects.none()

        formset = ArticleSystemeFormSet(request.POST, queryset=articles_qs)

        if form.is_valid() and formset.is_valid():
            systeme = form.save()

            systeme.articles.clear()

            for f in formset:
                if f.cleaned_data.get('ajouter'):
                    article = f.instance
                    article.qte = f.cleaned_data.get('qte', 0)
                    article.prix = f.cleaned_data.get('prix', 0)
                    article.save()
                    systeme.articles.add(article)

            return redirect('systeme_list')

        print("FORM ERRORS:", form.errors)
        print("FORMSET ERRORS:", formset.errors)

    else:
        form = SystemeForm(instance=systeme)

        # Articles du type + déjà liés
        articles_qs = (
            Article.objects.filter(systeme_types=systeme.type) |
            systeme.articles.all()
        ).distinct()

        # Pré-remplissage
        initial_data = []
        for art in articles_qs:
            initial_data.append({
                'qte': art.qte,
                'prix': art.prix,
                'ajouter': art in systeme.articles.all()
            })

        formset = ArticleSystemeFormSet(
            queryset=articles_qs,
            initial=initial_data
        )

    return render(request, "systeme/edit.html", {
        "form": form,
        "formset": formset,
        "systeme": systeme
    })

def delete(request, pk):
    systeme = get_object_or_404(Systeme, pk=pk)

    if request.method == "POST":
        systeme.delete()
        return redirect("systeme_list")

    return render(request, "systeme/delete.html", {"systeme": systeme})