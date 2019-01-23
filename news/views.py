from rest_framework import generics

from news.models import News
from news.serializers import NewsSerializer


class NewsDetail(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class LatestNews(generics.ListAPIView):
    queryset = News.objects.all().order_by("-pub_date")[:5]
    serializer_class = NewsSerializer


class LatestNewsSoccer(generics.ListAPIView):
    queryset = News.objects.all().filter(sport='Soccer').order_by("-pub_date")[:5]
    serializer_class = NewsSerializer


class LatestNewsBasketball(generics.ListAPIView):
    queryset = News.objects.all().filter(sport='Basketball').order_by("-pub_date")[:5]
    serializer_class = NewsSerializer
