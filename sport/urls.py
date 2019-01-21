from django.urls import path

from . import views

urlpatterns = [
    path('soccer/statistic/<int:pk>/', views.SoccerPlayerStatistics.as_view(), name='soccer_player_statistic'),
    path('basketball/statistic/<int:pk>/', views.BasketballPlayerStatistics.as_view(),
         name='basketball_player_statistic'),
    path('soccer/statistic/<int:pk>/', views.SoccerPlayerStatistics.as_view(), name='soccer_player_statistic'),
    path('basketball/statistic/<int:pk>/', views.BasketballPlayerStatistics.as_view(), name='basketball_player_statistic'),
    path('player/related_news/<int:pk>/', views.PlayerRelatedNews.as_view(), name='player_related_news'),
    path('team/related_news/<int:pk>/', views.TeamRelatedNews.as_view(), name='team_related_news'),
    path('soccer/player/<int:pk>/', views.SoccerPlayerInfo.as_view(), name='soccer_player_info'),
    path('basketball/player/<int:pk>/', views.BasketballPlayerInfo.as_view(), name='basketball_player_info'),
    path('person/images/<int:pk>/', views.PlayerImages.as_view(), name='player_images'),
]
