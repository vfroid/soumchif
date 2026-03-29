from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, filters
from article.models import Article
from article.api.serializers import ArticleSerializer
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render

class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    #permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()

    # 🔹 Ajouter la possibilité de rechercher par nom
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom']


def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'article/list_articles.html', {'articles': articles})