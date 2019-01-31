from rest_framework.serializers import ModelSerializer

from authentication.serializers import CustomUserDetailsSerializer
from news.models import Comment, News, Tag


class CommentSerializer(ModelSerializer):
    author = CustomUserDetailsSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class NewsSerializer(ModelSerializer):
    author = CustomUserDetailsSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = News
        fields = (
            'id', 'sport', 'author', 'title', 'brief', 'text', 'pub_date', 'image', 'tags', 'related_news', 'comments')
        depth = 2


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
