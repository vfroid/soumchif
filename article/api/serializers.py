from rest_framework.serializers import ModelSerializer

from article.models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'nom','groupe','sous_groupe','unite','qte','prix','montant']