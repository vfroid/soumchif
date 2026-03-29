from django import forms
from .models import Projet

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['mandant','description']   # P.S debut est non modifiable
        labels = {
            'mandant': "Mandant",
            'description' : "Description",
            'debut': "Date de début",
        }
        widgets = {
            'mandant': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'debut': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
