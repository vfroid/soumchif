from django.urls import path
import calorifu.views

urlpatterns=[
    path('calorifu/list',calorifu.views.list, name='calorifu_list'),
    path('calorifu/new',calorifu.views.new,name='calorifu_new'),
    path('calorifu/<int:pk>/edit/',calorifu.views.edit,name='calorifu_edit'),
    path('calorifu/<int:pk>/show/',calorifu.views.show,name='calorifu_show'),
    path('calorifu/<int:pk>/delete/', calorifu.views.delete, name='calorifu_delete'),

]