from rest_framework.serializers import ModelSerializer

from authentication.serializers import CustomUserDetailsSerializer
from news.models import Comment, News, Tag


class NewsSerializer(ModelSerializer):
    author = CustomUserDetailsSerializer()

    class Meta:
        model = News
        fields = '__all__'
        depth = 1


class CommentSerializer(ModelSerializer):
    author = CustomUserDetailsSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
