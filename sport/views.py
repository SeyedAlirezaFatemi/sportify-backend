from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics

from news.models import News
from news.serializers import NewsSerializer
from sport.models import BasketballEvent, BasketballGame, BasketballPlayer, BasketballTeam, BasketballTeamImage, \
    BasketballTeamLeagueStatistic, League, Person, SoccerEvent, SoccerGame, SoccerPlayer, SoccerTeam, SoccerTeamImage, \
    SoccerTeamLeagueStatistic
from sport.serializers.game_serializer import BasketballEventSerializer, BasketballGameSerializer, \
    BasketballGameStatisticsSerializer, BasketballImagesSerializer, BasketballTeamImageSerializer, \
    BasketballTeamLeagueStatisticSerializer, BasketballTeamSerializer, LeagueSerializer, SoccerEventSerializer, \
    SoccerGameSerializer, SoccerGameStatisticsSerializer, SoccerImagesSerializer, SoccerTeamImageSerializer, \
    SoccerTeamLeagueStatisticSerializer, SoccerTeamSerializer
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
        person = get_object_or_404(Person, pk=player_id)
        name = person.name
        queryset = News.objects.filter(Q(title__icontains=name) | Q(brief__icontains=name)
                                       | Q(text__icontains=name) | Q(tags__title__icontains=name))
        return queryset


# basketball game -> related news
class BasketballGameRelatedNews(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        game_id = self.kwargs['pk']
        game = get_object_or_404(BasketballGame, pk=game_id)
        home_team_name = game.home.team.name
        away_team_name = game.away.team.name

        queryset = News.objects.filter((Q(title__icontains=home_team_name) & Q(title__icontains=away_team_name)) |
                                       (Q(brief__icontains=home_team_name) & Q(brief__icontains=away_team_name)) |
                                       (Q(text__icontains=home_team_name) & Q(text__icontains=away_team_name)) |
                                       (Q(tags__title__icontains=home_team_name) & Q(
                                           tags__title__icontains=away_team_name)))
        return queryset


# SoccerGame_id -> RelatedNews
class SoccerGameRelatedNews(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        game_id = self.kwargs['pk']
        game = get_object_or_404(SoccerGame, pk=game_id)
        home_team_name = game.home.team.name
        away_team_name = game.away.team.name

        queryset = News.objects.filter((Q(title__icontains=home_team_name) & Q(title__icontains=away_team_name)) |
                                       (Q(brief__icontains=home_team_name) & Q(brief__icontains=away_team_name)) |
                                       (Q(text__icontains=home_team_name) & Q(text__icontains=away_team_name)) |
                                       (Q(tags__title__icontains=home_team_name) & Q(
                                           tags__title__icontains=away_team_name)))
        return queryset


# Team_id -> Related News
class SoccerTeamRelatedNews(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        team = get_object_or_404(SoccerTeam, pk=team_id)
        name = team.name
        queryset = News.objects.filter(Q(title__icontains=name) | Q(brief__icontains=name)
                                       | Q(text__icontains=name) | Q(tags__title__icontains=name))
        return queryset


# Team_id -> Related News
class BasketballTeamRelatedNews(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        team = get_object_or_404(BasketballTeam, pk=team_id)
        name = team.name
        queryset = News.objects.filter(Q(title__icontains=name) | Q(brief__icontains=name)
                                       | Q(text__icontains=name) | Q(tags__title__icontains=name))
        return queryset


# Team_id -> TeamPlayers
class SoccerTeamPlayers(generics.ListAPIView):
    serializer_class = SoccerPlayerSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        team = get_object_or_404(SoccerTeam, pk=team_id)
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
        team_games = SoccerGame.objects.filter(Q(home__team__id=team_id) |
                                               Q(away__team__id=team_id)).only('home__team__name',
                                                                               'away__team__name',
                                                                               'home__goals',
                                                                               'away__goals')

        return team_games


class BasketballTeamGameSchedule(generics.ListAPIView):
    serializer_class = BasketballGameSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        team_games = BasketballGame.objects.filter(Q(home__team__id=team_id) |
                                                   Q(away__team__id=team_id)).only('home__team__name',
                                                                                   'away__team__name',
                                                                                   'home__goals',
                                                                                   'away__goals')
        return team_games


# Game_id -> GameEvents
class BasketballEvents(generics.ListAPIView):
    serializer_class = BasketballEventSerializer

    def get_queryset(self):
        game_id = self.kwargs['pk']
        game_events = BasketballEvent.objects.filter(game_id=game_id)
        return game_events


# Game_id -> GameEvents
class SoccerEvents(generics.ListAPIView):
    serializer_class = SoccerEventSerializer

    def get_queryset(self):
        game_id = self.kwargs['pk']
        game_events = SoccerEvent.objects.filter(game_id=game_id)
        return game_events


# team_id => team images
class BasketballTeamImages(generics.ListAPIView):
    serializer_class = BasketballTeamImageSerializer

    def get_queryset(self):
        return BasketballTeamImage.objects.filter(team_id=self.kwargs['pk'])


class SoccerTeamImages(generics.ListAPIView):
    serializer_class = SoccerTeamImageSerializer

    def get_queryset(self):
        return SoccerTeamImage.objects.filter(team_id=self.kwargs['pk'])


# All leagues
class Leagues(generics.ListAPIView):
    serializer_class = LeagueSerializer
    queryset = League.objects.all()


# League_id => SoccerLeagueStatistics
class SoccerLeagueStats(generics.ListAPIView):
    serializer_class = SoccerTeamLeagueStatisticSerializer

    def get_queryset(self):
        league_id = self.kwargs['pk']
        queryset = SoccerTeamLeagueStatistic.objects.all().filter(league_id=league_id)
        return queryset


# League_id => BasketballLeagueStatistics
class BasketballLeagueStats(generics.ListAPIView):
    serializer_class = BasketballTeamLeagueStatisticSerializer

    def get_queryset(self):
        league_id = self.kwargs['pk']
        queryset = BasketballTeamLeagueStatistic.objects.all().filter(league_id=league_id)
        return queryset
