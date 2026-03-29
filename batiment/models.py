from django.db import models

from projet.models import Projet

class Batiment(models.Model):
    projet= models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='batiments_batiment')
    nom = models.CharField(max_length=100)
    cp = models.IntegerField(default=0)
    rue =  models.CharField(max_length=50, blank=True)
    ville = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nom

class Etage(models.Model):
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE, related_name='etages')
    numero = models.IntegerField()
    # Pour les étages spéciaux comme le sous-sol ou le rez-de-chaussée
    designation = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return f"{self.batiment} - {self.designation or f'Étage {self.numero}'}"

class Local(models.Model):
    etage = models.ForeignKey(Etage, on_delete=models.CASCADE, related_name='locals')
    code = models.CharField(max_length=20)
    designation = models.CharField(max_length=100)
    surface = models.FloatField(help_text="Surface en m²")
    qint = models.FloatField(help_text="Température intérieure en °C")
    qe = models.FloatField(help_text="Température extérieure en °C")
    FT = models.FloatField(help_text="Flux thermique en W")
    FV = models.FloatField(help_text="Flux ventilation en W")
    Fg = models.FloatField(help_text="Flux gains en W")
    FHL = models.FloatField(help_text="Flux chauffage en W")
    fapostehl = models.FloatField(help_text="Flux aposté en W/m²")
    nmin = models.FloatField(help_text="Taux de renouvellement d'air en h⁻¹")

    def __str__(self):
        return f"{self.etage} - {self.code} ({self.designation})"