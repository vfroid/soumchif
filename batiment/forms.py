from django import forms

from .models import Batiment,Etage,Local,Projet


class BatimentForm(forms.ModelForm):
    class Meta:
        model = Batiment
        fields = ['projet', 'nom', 'cp', 'rue', 'ville']
        labels = {
            'projet': "Projet",
            'nom': "Nom du bâtiment",
            'cp': "Code postal",
            'rue': "Rue",
            'ville': "Ville",
        }
        widgets = {
            'projet': forms.Select(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'cp': forms.NumberInput(attrs={'class': 'form-control'}),
            'rue': forms.TextInput(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['projet'].queryset = Projet.objects.all()



class EtageForm(forms.ModelForm):
    class Meta:
        model = Etage
        fields = ['batiment', 'numero', 'designation']
        labels = {
            'batiment': "Bâtiment",
            'numero': "Numéro de l'étage",
            'designation': "Désignation (optionnelle)",
        }
        widgets = {
            'batiment': forms.Select(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Sous-sol, Rez-de-chaussée'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['batiment'].queryset = Batiment.objects.all()




class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = [
            'etage', 'code', 'designation',
            'surface', 'qint', 'qe',
            'FT', 'FV', 'Fg', 'FHL',
            'fapostehl', 'nmin'
        ]
        labels = {
            'etage': "Étage",
            'code': "Code",
            'designation': "Désignation",
            'surface': "Surface (m²)",
            'qint': "Température intérieure (°C)",
            'qe': "Température extérieure (°C)",
            'FT': "Flux thermique (W)",
            'FV': "Flux ventilation (W)",
            'Fg': "Flux gains (W)",
            'FHL': "Flux chauffage (W)",
            'fapostehl': "Flux aposté (W/m²)",
            'nmin': "Taux de renouvellement d'air (h⁻¹)",
        }
        help_texts = {
            'surface': "Surface en m²",
            'qint': "Température intérieure en °C",
            'qe': "Température extérieure en °C",
            'FT': "Flux thermique en W",
            'FV': "Flux ventilation en W",
            'Fg': "Flux gains en W",
            'FHL': "Flux chauffage en W",
            'fapostehl': "Flux aposté en W/m²",
            'nmin': "Taux de renouvellement d'air en h⁻¹",
        }
        widgets = {
            'etage': forms.Select(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'surface': forms.NumberInput(attrs={'class': 'form-control'}),
            'qint': forms.NumberInput(attrs={'class': 'form-control'}),
            'qe': forms.NumberInput(attrs={'class': 'form-control'}),
            'FT': forms.NumberInput(attrs={'class': 'form-control'}),
            'FV': forms.NumberInput(attrs={'class': 'form-control'}),
            'Fg': forms.NumberInput(attrs={'class': 'form-control'}),
            'FHL': forms.NumberInput(attrs={'class': 'form-control'}),
            'fapostehl': forms.NumberInput(attrs={'class': 'form-control'}),
            'nmin': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['projet'].queryset = Etage.objects.all()
