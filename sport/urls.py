from django.urls import path

from . import views

urlpatterns = [
    path('statistic/soccer/<int:pk>/', views.SoccerPlayerStatistics.as_view(), name='soccer_player_statistic'),
    path('statistic/basketball/<int:pk>/', views.BasketballPlayerStatistics.as_view(),
         name='basketball_player_statistic'),

    path('player/related_news/<int:pk>/', views.PlayerRelatedNews.as_view(), name='player_related_news'),
    path('player/soccer/<int:pk>/', views.SoccerPlayerInfo.as_view(), name='soccer_player_info'),
    path('player/basketball/<int:pk>/', views.BasketballPlayerInfo.as_view(), name='basketball_player_info'),

    path('player/soccer/images/<int:pk>/', views.SoccerPlayerImages.as_view(), name='soccer_player_images'),
    path('player/basketball/images/<int:pk>/', views.BasketballPlayerImages.as_view(), name='basketball_player_images'),

    path('players/soccer/<int:pk>/', views.SoccerTeamPlayers.as_view(), name='soccer_team_players'),
    path('players/basketball/<int:pk>/', views.BasketballTeamPlayers.as_view(), name='soccer_team_players'),

    path('leagues/latest/<int:pk>/', views.LatestLeagues.as_view(), name='latest_leagues'),
    path('league/<int:pk>/', views.LeagueInfo.as_view(), name='league_info'),

    path('teams/related_news/<int:pk>/', views.TeamRelatedNews.as_view(), name='team_related_news'),
    path('team/soccer/<int:pk>/', views.SoccerTeamInfo.as_view(), name='soccer_team_info'),
    path('team/basketball/<int:pk>/', views.BasketballTeamInfo.as_view(), name='basketball_team_info'),
    path('team/soccer/schedule/<int:pk>/', views.SoccerTeamGameSchedule.as_view(), name='soccer_team_schedule'),
    path('team/basketball/schedule/<int:pk>/', views.BasketballTeamGameSchedule.as_view(),
         name='basketball_team_schedule'),

    path('game/soccer/images/<int:pk>/', views.SoccerGameImages.as_view(), name='soccer_game_images'),
    path('game/basketball/images/<int:pk>/', views.BasketballGameImages.as_view(), name='basketball_game_images'),
    path('games/soccer/yesterday/', views.YesterdaySoccerGame.as_view(), name='yesterday_soccer_game'),
    path('games/soccer/tomorrow/', views.TomorrowSoccerGame.as_view(), name='tomorrow_soccer_game'),
    path('games/soccer/today/', views.TodaySoccerGame.as_view(), name='today_soccer_game'),
    path('games/basketball/yesterday/', views.YesterdayBasketballGame.as_view(), name='yesterday_basketball_game'),
    path('games/basketball/tomorrow/', views.TomorrowBasketballGame.as_view(), name='tomorrow_basketball_game'),
    path('games/basketball/today/', views.TodayBasketballGame.as_view(), name='today_basketball_game'),
    path('games/soccer/latest/<int:pk>/', views.LatestSoccerGames.as_view(), name='latest_soccer_games'),
    path('games/basketball/latest/<int:pk>/', views.LatestBasketballGames.as_view(), name='latest_basketball_games'),
]
