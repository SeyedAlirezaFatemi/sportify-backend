from django.urls import path

from . import views

urlpatterns = [
    path('soccer/statistic/', views.SoccerPlayerStatistics.as_view(), name='soccer_player_statistic'),
    path('basketball/statistic/', views.BasketballPlayerStatistics.as_view(), name='basketball_player_statistic'),
]
