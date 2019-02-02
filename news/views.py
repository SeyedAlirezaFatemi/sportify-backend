from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from news.models import Comment, News
from news.serializers import NewsSerializer


class NewsDetail(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class LatestNews(generics.ListAPIView):
    queryset = News.objects.all().order_by("-pub_date")
    serializer_class = NewsSerializer


class LatestNewsSoccer(generics.ListAPIView):
    queryset = News.objects.all().filter(sport='Soccer').order_by("-pub_date")
    serializer_class = NewsSerializer
    # pagination_class = LimitOffsetPagination


class LatestNewsBasketball(generics.ListAPIView):
    queryset = News.objects.all().filter(sport='Basketball').order_by("-pub_date")
    serializer_class = NewsSerializer
    # pagination_class = LimitOffsetPagination


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def comment(request):
    commenter = request.user
    try:
        news_id = request.data['news_id']
        comment_text = request.data['comment_text']
        news = get_object_or_404(News, pk=news_id)
        if not comment_text:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        Comment.objects.create(author=commenter, text=comment_text, pub_date=timezone.now(), news=news)
        return Response(status=status.HTTP_201_CREATED)
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
