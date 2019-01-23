from django.urls import path

from . import views

urlpatterns = [

    path('player/statistics/soccer/<int:pk>/', views.SoccerPlayerStatistics.as_view(), name='soccer_player_statistics'),
    path('player/statistics/basketball/<int:pk>/', views.BasketballPlayerStatistics.as_view(),
         name='basketball_player_statistics'),

    path('player/related_news/<int:pk>/', views.PlayerRelatedNews.as_view(), name='player_related_news'),

    path('player/soccer/info/<int:pk>/', views.SoccerPlayerInfo.as_view(), name='soccer_player_info'),
    path('player/basketball/info/<int:pk>/', views.BasketballPlayerInfo.as_view(), name='basketball_player_info'),

    path('player/soccer/images/<int:pk>/', views.SoccerPlayerImages.as_view(), name='soccer_player_images'),
    path('player/basketball/images/<int:pk>/', views.BasketballPlayerImages.as_view(), name='basketball_player_images'),

    path('team/players/soccer/<int:pk>/', views.SoccerTeamPlayers.as_view(), name='soccer_team_players'),
    path('team/players/basketball/<int:pk>/', views.BasketballTeamPlayers.as_view(), name='basketball_team_players'),

    path('leagues/', views.Leagues.as_view(), name='leagues'),
    path('leagues/latest/<int:pk>/', views.LatestLeagues.as_view(), name='latest_leagues'),
    path('league/info/<int:pk>/', views.LeagueInfo.as_view(), name='league_info'),
    path('league/stats/soccer/<int:pk>/', views.SoccerLeagueStats.as_view(), name='soccer_league_stats'),
    path('league/stats/basketball/<int:pk>/', views.BasketballLeagueStats.as_view(), name='basketball_league_info'),

    path('team/soccer/related_news/<int:pk>/', views.SoccerTeamRelatedNews.as_view(), name='soccer_team_related_news'),
    path('team/basketball/related_news/<int:pk>/', views.BasketballTeamRelatedNews.as_view(),
         name='basketball_team_related_news'),

    path('team/soccer/info/<int:pk>/', views.SoccerTeamInfo.as_view(), name='soccer_team_info'),
    path('team/basketball/info/<int:pk>/', views.BasketballTeamInfo.as_view(), name='basketball_team_info'),

    path('team/soccer/schedule/<int:pk>/', views.SoccerTeamGameSchedule.as_view(), name='soccer_team_schedule'),
    path('team/basketball/schedule/<int:pk>/', views.BasketballTeamGameSchedule.as_view(),
         name='basketball_team_schedule'),
    path('team/soccer/images/<int:pk>/', views.SoccerTeamImages.as_view(), name='soccer_team_images'),
    path('team/basketball/images/<int:pk>/', views.BasketballTeamImages.as_view(), name='basketball_team_images'),

    path('team/soccer/players/<int:pk>/', views.SoccerTeamPlayers.as_view(), name='soccer_team_players'),
    path('team/basketball/players/<int:pk>/', views.BasketballTeamPlayers.as_view(), name='basketball_team_players'),

    path('game/soccer/images/<int:pk>/', views.SoccerGameImages.as_view(), name='soccer_game_images'),
    path('game/basketball/images/<int:pk>/', views.BasketballGameImages.as_view(), name='basketball_game_images'),

    path('game/soccer/yesterday/', views.YesterdaySoccerGame.as_view(), name='yesterday_soccer_game'),
    path('game/soccer/tomorrow/', views.TomorrowSoccerGame.as_view(), name='tomorrow_soccer_game'),
    path('game/soccer/today/', views.TodaySoccerGame.as_view(), name='today_soccer_game'),

    path('game/basketball/yesterday/', views.YesterdayBasketballGame.as_view(), name='yesterday_basketball_game'),
    path('game/basketball/tomorrow/', views.TomorrowBasketballGame.as_view(), name='tomorrow_basketball_game'),
    path('game/basketball/today/', views.TodayBasketballGame.as_view(), name='today_basketball_game'),

    path('game/soccer/latest/<int:pk>/', views.LatestSoccerGames.as_view(), name='latest_soccer_games'),
    path('game/basketball/latest/<int:pk>/', views.LatestBasketballGames.as_view(), name='latest_basketball_games'),

    path('game/basketball/statistics/<int:pk>/', views.BasketballGameStatistics.as_view(),
         name='basketball_game_statistics'),
    path('game/soccer/statistics/<int:pk>/', views.SoccerGameStatistics.as_view(), name='soccer_game_statistics'),

    path('game/soccer/related_news/<int:pk>/', views.SoccerGameRelatedNews.as_view(), name='soccer_game_related_news'),
    path('game/basketball/related_news/<int:pk>/', views.BasketballGameRelatedNews.as_view(),
         name='basketball_game_related_news'),

    path('game/basketball/events/<int:pk>/', views.BasketballEvents.as_view(), name='basketball_game_events'),
    path('game/soccer/events/<int:pk>/', views.SoccerEvents.as_view(), name='soccer_game_events'),

]
