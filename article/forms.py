
from django import forms
from .models import Article
from systeme.models import Systeme



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['nom', 'groupe', 'sous_groupe', 'prix', 'unite', 'qte']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'groupe': forms.TextInput(attrs={'class': 'form-control'}),
            'sous_groupe': forms.TextInput(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'unite': forms.TextInput(attrs={'class': 'form-control'}),
            'qte': forms.NumberInput(attrs={'class': 'form-control'}),
        }

