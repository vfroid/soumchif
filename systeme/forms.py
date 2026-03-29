from django import forms
from django.forms import modelformset_factory
from systeme.models import Systeme
from article.models import Article
from batiment.models import Local
from projet.models import Projet

# Formulaire principal pour Systeme
class SystemeForm(forms.ModelForm):
    class Meta:
        model = Systeme
        fields = ['nom', 'abreviation', 'type', 'local', 'projet']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'abreviation': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Champs ForeignKey
        self.fields['local'].queryset = Local.objects.all()
        self.fields['projet'].queryset = Projet.objects.all()


# Formulaire pour chaque article lié ou proposé
class ArticleSystemeForm(forms.ModelForm):
    ajouter = forms.BooleanField(required=False, label="Ajouter cet article")

    class Meta:
        model = Article
        fields = ['qte', 'prix']  # champs modifiables pour ce système

# Formset basé sur ArticleSystemeForm
ArticleSystemeFormSet = modelformset_factory(
    Article,
    form=ArticleSystemeForm,
    extra=0  # pas de formulaire vide supplémentaire
)