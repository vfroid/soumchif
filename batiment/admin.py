from django.contrib import admin
from .models import Batiment, Etage, Local

@admin.register(Batiment)
class BatimentAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(Etage)
class EtageAdmin(admin.ModelAdmin):
    list_display = ('batiment', 'designation', 'numero')

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('etage', 'code', 'designation', 'surface')
    list_filter = ('etage__batiment', 'etage')
from django.contrib import admin

# Register your models here.
