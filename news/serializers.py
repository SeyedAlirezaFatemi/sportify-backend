from rest_framework.serializers import ModelSerializer

from news.models import Comment, News, Tag


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
