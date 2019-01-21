from django.urls import path

from . import views

urlpatterns = [
    path('soccer/statistic/<int:pk>/', views.SoccerPlayerStatistics.as_view(), name='soccer_player_statistic'),
    path('basketball/statistic/<int:pk>/', views.BasketballPlayerStatistics.as_view(),
         name='basketball_player_statistic'),
    path('player/related_news/<int:pk>/', views.PlayerRelatedNews.as_view(), name='player_related_news'),
    path('team/related_news/<int:pk>/', views.TeamRelatedNews.as_view(), name='team_related_news'),
    path('soccer/player/<int:pk>/', views.SoccerPlayerInfo.as_view(), name='soccer_player_info'),
    path('basketball/player/<int:pk>/', views.BasketballPlayerInfo.as_view(), name='basketball_player_info'),
    path('person/images/<int:pk>/', views.PlayerImages.as_view(), name='player_images'),
    path('soccer/players/<int:pk>/', views.SoccerTeamPlayers.as_view(), name='soccer_team_players'),
    path('basketball/players/<int:pk>/', views.BasketballTeamPlayers.as_view(), name='soccer_team_players'),
    path('leagues/latest/<int:pk>/', views.LatestLeagues.as_view(), name='latest_leagues'),
    path('league/<int:pk>/', views.LeagueInfo.as_view(), name='league_info'),
    path('soccer/game/images/<int:pk>/', views.SoccerGameImages.as_view(), name='soccer_game_images'),
    path('basketball/game/images/<int:pk>/', views.BasketballGameImages.as_view(), name='basketball_game_images'),
    path('game/soccer/yesterday/', views.YesterdaySoccerGame.as_view(), name='yesterday_soccer_game'),
    path('game/soccer/tomorrow/', views.TomorrowSoccerGame.as_view(), name='tomorrow_soccer_game'),
    path('game/soccer/today/', views.TodaySoccerGame.as_view(), name='today_soccer_game'),
    path('game/basketball/yesterday/', views.YesterdayBasketballGame.as_view(), name='yesterday_basketball_game'),
    path('game/basketball/tomorrow/', views.TomorrowBasketballGame.as_view(), name='tomorrow_basketball_game'),
    path('game/basketball/today/', views.TodayBasketballGame.as_view(), name='today_basketball_game'),
    path('game/soccer/latest/<int:pk>/', views.LatestSoccerGames.as_view(), name='latest_soccer_games'),
    path('game/basketball/latest/<int:pk>/', views.LatestBasketballGames.as_view(), name='latest_basketball_games'),
]
