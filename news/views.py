from rest_framework import generics

from news.models import News
from news.serializers import NewsSerializer


class LatestNews(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
