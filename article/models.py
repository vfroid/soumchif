
from django.conf import settings
from django.db import models

from systeme.models  import Systeme,SystemeType


class Article(models.Model):
    nom = models.CharField(max_length=100)
    groupe = models.CharField(max_length=50)
    sous_groupe = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unite = models.CharField(max_length=20)
    qte = models.PositiveIntegerField(default=0)

    @property
    def montant(self):
        try:
            return float(self.prix) * int(self.qte)
        except:
            return 0

    def __str__(self):
        return f"{self.nom} ({self.qte} {self.unite})"