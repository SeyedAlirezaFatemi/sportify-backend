from rest_framework.serializers import ModelSerializer

from news.models import News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
