from django.urls import path,include

import article.views

urlpatterns = [
    path('api/', include('article.api.urls')),
    path('article/list', article.views.list,name='article_list'),
    path('article/new/', article.views.new, name='article_new'),
    path('article/<int:pk>/edit/', article.views.edit, name='article_edit'),
    path('article/<int:pk>/delete/', article.views.delete, name='article_delete'),
    path('article/<int:pk>/', article.views.show, name='article_show'),
    path('article/list_articles', article.views.list_articles, name='article_list_articles'),
    path('<int:article_id>/attribuer_systemes/', article.views.attribuer_systemes, name='attribuer_systemes'),
]