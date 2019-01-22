from django.db.models import Q
from django.utils import timezone
from rest_framework import generics

from news.models import News
from news.serializers import NewsSerializer
from sport.models import BasketballGame, BasketballPlayer, BasketballTeam, League, Person, \
    SoccerGame, SoccerPlayer, SoccerTeam, Team
from sport.serializers.game_serializer import BasketballGameSerializer, BasketballImagesSerializer, \
    BasketballTeamSerializer, LeagueSerializer, SoccerGameSerializer, SoccerImagesSerializer, SoccerTeamSerializer, \
    SoccerGameStatisticsSerializer, BasketballGameStatisticsSerializer
from sport.serializers.player_serializer import BasketballPlayerImagesSerializer, BasketballPlayerSerializer, \
    BasketballPlayerStatisticsSerializer, SoccerPlayerImagesSerializer, SoccerPlayerSerializer, \
    SoccerPlayerStatisticsSerializer


# Player_id -> PlayerStatistics
class BasketballPlayerStatistics(generics.RetrieveAPIView):
    serializer_class = BasketballPlayerStatisticsSerializer
    queryset = BasketballPlayer.objects.all()


# Player_id -> PlayerStatistics
class SoccerPlayerStatistics(generics.RetrieveAPIView):
    serializer_class = SoccerPlayerStatisticsSerializer
    queryset = SoccerPlayer.objects.all()


# Game_id -> SoccerGameStatistics
class SoccerGameStatistics(generics.RetrieveAPIView):
    serializer_class = SoccerGameStatisticsSerializer
    queryset = SoccerGame.objects.all()


# Game_id -> BasketballGameStatistics
class BasketballGameStatistics(generics.RetrieveAPIView):
    serializer_class = BasketballGameStatisticsSerializer
    queryset = BasketballGame.objects.all()


# Player_id -> Related News
class PlayerRelatedNews(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        player_id = self.kwargs['pk']
        person = Person.objects.get(id=player_id)
        name = person.name
        queryset = News.objects.filter(Q(title__contains=name) | Q(brief__contains=name)
                                       | Q(text__contains=name) | Q(tags__title__contains=name))
        return queryset


# Team_id -> Related News
class TeamRelatedNews(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        team = Team.objects.get(id=team_id)
        name = team.name
        queryset = News.objects.filter(Q(title__contains=name) | Q(brief__contains=name)
                                       | Q(text__contains=name) | Q(tags__title__contains=name))
        return queryset


# Team_id -> TeamPlayers
class SoccerTeamPlayers(generics.ListAPIView):
    serializer_class = SoccerPlayerSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        team = SoccerTeam.objects.get(id=team_id)
        # team.soccerplayer_set.all()
        queryset = SoccerPlayer.objects.filter(team=team)
        return queryset


# Team_id -> TeamPlayers
class BasketballTeamPlayers(generics.ListAPIView):
    serializer_class = SoccerPlayerSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        queryset = BasketballPlayer.objects.filter(team_id=team_id)
        return queryset


# Player_id -> PlayerInfo
class SoccerPlayerInfo(generics.RetrieveAPIView):
    queryset = SoccerPlayer.objects.all()
    serializer_class = SoccerPlayerSerializer


# Player_id -> PlayerInfo
class BasketballPlayerInfo(generics.RetrieveAPIView):
    queryset = BasketballPlayer.objects.all()
    serializer_class = BasketballPlayerSerializer


# Game_id -> GameImages
class SoccerGameImages(generics.RetrieveAPIView):
    queryset = SoccerGame.objects.all()
    serializer_class = SoccerImagesSerializer


# Game_id -> GameImages
class BasketballGameImages(generics.RetrieveAPIView):
    queryset = BasketballGame.objects.all()
    serializer_class = BasketballImagesSerializer


# Player_id -> PlayerImages
class SoccerPlayerImages(generics.ListAPIView):
    serializer_class = SoccerPlayerImagesSerializer
    queryset = SoccerPlayer.objects.all()


# Player_id -> PlayerImages
class BasketballPlayerImages(generics.ListAPIView):
    serializer_class = BasketballPlayerImagesSerializer
    queryset = BasketballPlayer.objects.all()


# Latest Leagues
class LatestLeagues(generics.ListAPIView):
    serializer_class = LeagueSerializer
    queryset = League.objects.all().order_by('-beginning_year')[:5]


# League_id -> LeagueInfo
class LeagueInfo(generics.RetrieveAPIView):
    serializer_class = LeagueSerializer
    queryset = League.objects.all()


class YesterdaySoccerGame(generics.ListAPIView):
    yesterday = timezone.now() - timezone.timedelta(days=1)
    serializer_class = SoccerGameSerializer
    queryset = SoccerGame.objects.filter(Q(play_date__year=yesterday.year) &
                                         Q(play_date__month=yesterday.month) &
                                         Q(play_date__day=yesterday.day))


class TomorrowSoccerGame(generics.ListAPIView):
    tomorrow = timezone.now() + timezone.timedelta(days=1)
    serializer_class = SoccerGameSerializer
    queryset = SoccerGame.objects.filter(Q(play_date__year=tomorrow.year) &
                                         Q(play_date__month=tomorrow.month) &
                                         Q(play_date__day=tomorrow.day))


class TodaySoccerGame(generics.ListAPIView):
    serializer_class = SoccerGameSerializer
    queryset = SoccerGame.objects.filter(Q(play_date__year=timezone.now().year) &
                                         Q(play_date__month=timezone.now().month) &
                                         Q(play_date__day=timezone.now().day))


class YesterdayBasketballGame(generics.ListAPIView):
    yesterday = timezone.now() - timezone.timedelta(days=1)
    serializer_class = BasketballGameSerializer
    queryset = BasketballGame.objects.filter(Q(play_date__year=yesterday.year) &
                                             Q(play_date__month=yesterday.month) &
                                             Q(play_date__day=yesterday.day))


class TomorrowBasketballGame(generics.ListAPIView):
    tomorrow = timezone.now() + timezone.timedelta(days=1)
    serializer_class = BasketballGameSerializer
    queryset = BasketballGame.objects.filter(Q(play_date__year=tomorrow.year) &
                                             Q(play_date__month=tomorrow.month) &
                                             Q(play_date__day=tomorrow.day))


class TodayBasketballGame(generics.ListAPIView):
    serializer_class = BasketballGameSerializer
    queryset = BasketballGame.objects.filter(Q(play_date__year=timezone.now().year) &
                                             Q(play_date__month=timezone.now().month) &
                                             Q(play_date__day=timezone.now().day))


class LatestSoccerGames(generics.ListAPIView):
    serializer_class = SoccerGameSerializer
    queryset = SoccerGame.objects.all().order_by('-play_date')[:5]


class LatestBasketballGames(generics.ListAPIView):
    serializer_class = BasketballGameSerializer
    queryset = BasketballGame.objects.all().order_by('-play_date')[:5]


# SoccerTeam_id -> SoccerTeamInfo
class SoccerTeamInfo(generics.RetrieveAPIView):
    queryset = SoccerTeam.objects.all()
    serializer_class = SoccerTeamSerializer


# BasketballTeam_id -> SoccerTeamInfo
class BasketballTeamInfo(generics.RetrieveAPIView):
    queryset = BasketballTeam.objects.all()
    serializer_class = BasketballTeamSerializer


class SoccerTeamGameSchedule(generics.ListAPIView):
    serializer_class = SoccerGameSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        unfinished_team_games = SoccerGame.objects.filter((Q(home__team__id=team_id) |
                                                           Q(away__team__id=team_id)) &
                                                          Q(play_date__gte=timezone.now()))
        finished_team_games = SoccerGame.objects.filter((Q(home__team__id=team_id) |
                                                         Q(away__team__id=team_id)) &
                                                        Q(play_date__lt=timezone.now()))
        return unfinished_team_games


class BasketballTeamGameSchedule(generics.ListAPIView):
    serializer_class = BasketballGameSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        unfinished_team_games = BasketballGame.objects.filter((Q(home__team__id=team_id) |
                                                               Q(away__team__id=team_id)) &
                                                              Q(play_date__gte=timezone.now()))
        finished_team_games = BasketballGame.objects.filter((Q(home__team__id=team_id) |
                                                             Q(away__team__id=team_id)) &
                                                            Q(play_date__lt=timezone.now()))
        return unfinished_team_games
