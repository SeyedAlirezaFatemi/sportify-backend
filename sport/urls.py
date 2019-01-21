from django.urls import path

from . import views

urlpatterns = [
    path('soccer/statistic/<int:pk>', views.SoccerPlayerStatistics.as_view(), name='soccer_player_statistic'),
    path('basketball/statistic/<int:pk>', views.BasketballPlayerStatistics.as_view(), name='basketball_player_statistic'),
    path('related_news/<int:pk>', views.PlayerRelatedNews.as_view(), name='related_news')
]
