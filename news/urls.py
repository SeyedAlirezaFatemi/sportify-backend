from django.urls import path

from . import views

urlpatterns = [
    path('latest/', views.LatestNews.as_view(), name='latest_news'),
    path('detail/<int:pk>/', views.NewsDetail.as_view(), name='news_detail'),
]
