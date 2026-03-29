from django.urls import path,include

import batiment.views

urlpatterns = [
    path('batiment/list', batiment.views.list,name='batiment_list'),
    path('batiment/new', batiment.views.new,name='batiment_new'),
    path('batiment/<int:pk>/show', batiment.views.show,name='batiment_show'),
    path('batiment/<int:pk>/edit', batiment.views.edit,name='batiment_edit'),
    path('batiment/<int:pk>/delete', batiment.views.delete,name='batiment_delete'),
    path('batiment/<int:pk>/treeview', batiment.views.treeview_batiment,name='batiment_treeview'),
]