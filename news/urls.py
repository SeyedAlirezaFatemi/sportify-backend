from django.urls import path

from . import views

urlpatterns = [
    path('latest/', views.LatestNews.as_view(), name='latest_news'),

    path('latest/soccer/', views.LatestNewsSoccer.as_view(), name='latest_soccer_news'),
    path('latest/basketball/', views.LatestNewsBasketball.as_view(), name='latest_basketball_news'),

    path('detail/<int:pk>/', views.NewsDetail.as_view(), name='news_detail'),
]
