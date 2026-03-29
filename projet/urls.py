from django.urls import path

import projet.views



urlpatterns = [
    path('projet/', projet.views.list, name='projet_list'),
    path('projet/new', projet.views.new, name='projet_new'),
    path('projet/<int:pk>/show', projet.views.show, name='projet_show'),
    path('projet/<int:pk>/edit/', projet.views.edit, name='projet_edit'),
    path('projet/<int:pk>/delete/', projet.views.delete, name='projet_delete'),
]
