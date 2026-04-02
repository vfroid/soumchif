from django.urls import path

import projet.views



urlpatterns = [
    # Projets
    path('projet/', projet.views.projet_list, name='projet_list'),
    path('projet/new/', projet.views.new, name='projet_new'),
    path('projet/<int:pk>/show/', projet.views.show, name='projet_show'),
    path('projet/<int:pk>/edit/', projet.views.edit, name='projet_edit'),
    path('projet/<int:pk>/delete/', projet.views.delete, name='projet_delete'),

    # Articles
    path('projet/<int:pk>/articles/systeme/', projet.views.articles_par_systeme, name='projet_articles_par_systeme'),
    path('projet/<int:pk>/articles/global/', projet.views.articles_global, name='articles_global'),

    # Calorifugeage
    path('projet/<int:pk>/calorifugeage/systeme/', projet.views.calorifugeage_par_systeme, name='calorifugeage_par_systeme'),
    path('projet/<int:pk>/calorifugeage/global/', projet.views.calorifugeage_global, name='calorifugeage_global'),

    # Bâtiments
    path('projet/<int:pk>/batiments/', projet.views.projet_batiments, name='projet_batiments'),
]