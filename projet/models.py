from django.db import models
from django.db.models import Sum, F

class Projet(models.Model):
    mandant=models.CharField(max_length=100, blank=False)
    description=models.CharField(max_length=100, blank=False, default='')
    debut = models.DateTimeField(auto_now_add=True)

    def montant_total(self):
        return self.systemes.aggregate(
            total=Sum(F('articles__prix') * F('articles__qte'))
        )['total'] or 0

    def __str__(self):
        return f"{self.mandant} - {self.debut}"
