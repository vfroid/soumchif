from django.urls import path, include
from rest_framework import routers
from article.api.views import ArticleViewSet

router = routers.SimpleRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),  # <-- juste '', pas 'api/'
]