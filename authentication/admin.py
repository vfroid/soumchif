from django.contrib import admin

from authentication.models import User

class UserAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('username','email') # liste les champs que nous voulons sur l'affichage de la liste


admin.site.register(User,UserAdmin)
