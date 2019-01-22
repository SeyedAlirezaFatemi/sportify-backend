from django.db.models import Q
from django.utils import timezone
from rest_framework import generics

from news.models import News
from news.serializers import NewsSerializer
from sport.models import BasketballGame, BasketballPlayer, BasketballPlayerSeason, BasketballTeam, League, Person, \
    PlayerImage, SoccerGame, SoccerPlayer, SoccerPlayerSeason, SoccerTeam, Team
from sport.serializers.game_serializer import BasketballGameSerializer, BasketballImagesSerializer, \
    BasketballTeamSerializer, LeagueSerializer, SoccerGameSerializer, SoccerImagesSerializer, SoccerTeamSerializer
from sport.serializers.player_serializer import BasketballPlayerSeasonSerializer, BasketballPlayerSerializer, \
    PersonSerializer, SoccerPlayerSeasonSerializer, SoccerPlayerSerializer


class BasketballPlayerStatistics(generics.RetrieveAPIView):
    serializer_class = BasketballPlayerSeasonSerializer
    queryset = BasketballPlayerSeason.objects.all()


class SoccerPlayerStatistics(generics.RetrieveAPIView):
    queryset = SoccerPlayerSeason.objects.all()
    serializer_class = SoccerPlayerSeasonSerializer


class PlayerRelatedNews(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        player_id = self.kwargs['pk']
        person = Person.objects.get(id=player_id)
        name = person.name
        queryset = News.objects.filter(Q(title__contains=name) | Q(brief__contains=name)
                                       | Q(text__contains=name) | Q(tags__title__contains=name))
        return queryset


class TeamRelatedNews(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        team = Team.objects.get(id=team_id)
        name = team.name
        queryset = News.objects.filter(Q(title__contains=name) | Q(brief__contains=name)
                                       | Q(text__contains=name) | Q(tags__title__contains=name))
        return queryset


class SoccerTeamPlayers(generics.ListAPIView):
    serializer_class = SoccerPlayerSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        team = SoccerTeam.objects.get(id=team_id)
        queryset = SoccerPlayer.objects.filter(team=team)
        return queryset


class BasketballTeamPlayers(generics.ListAPIView):
    serializer_class = SoccerPlayerSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        queryset = BasketballPlayer.objects.filter(team_id=team_id)
        return queryset


class SoccerPlayerInfo(generics.RetrieveAPIView):
    queryset = SoccerPlayer.objects.all()
    serializer_class = SoccerPlayerSerializer


class BasketballPlayerInfo(generics.RetrieveAPIView):
    queryset = BasketballPlayer.objects.all()
    serializer_class = BasketballPlayerSerializer


class SoccerGameImages(generics.RetrieveAPIView):
    queryset = SoccerGame.objects.all()
    serializer_class = SoccerImagesSerializer


class BasketballGameImages(generics.RetrieveAPIView):
    queryset = BasketballGame.objects.all()
    serializer_class = BasketballImagesSerializer


class PlayerImages(generics.ListAPIView):
    serializer_class = PersonSerializer
    queryset = PlayerImage.objects.all()


class LatestLeagues(generics.ListAPIView):
    serializer_class = LeagueSerializer
    queryset = League.objects.all().order_by('-beginning_year')[:5]


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


class SoccerTeamInfo(generics.RetrieveAPIView):
    queryset = SoccerTeam.objects.all()
    serializer_class = SoccerTeamSerializer


class BasketballTeamInfo(generics.RetrieveAPIView):
    queryset = BasketballTeam.objects.all()
    serializer_class = BasketballTeamSerializer


class SoccerTeamGameSchedule(generics.ListAPIView):
    serializer_class = SoccerGameSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        unfinished_team_games = SoccerGame.objects.filter((Q(home__team__id=team_id) |
                                                           Q(away__team__id=team_id)) & Q(
            play_date__gte=timezone.now()))
        finished_team_games = SoccerGame.objects.filter((Q(home__team__id=team_id) |
                                                         Q(away__team__id=team_id)) & Q(play_date__lt=timezone.now()))
        return unfinished_team_games


class BasketballTeamGameSchedule(generics.ListAPIView):
    serializer_class = BasketballGameSerializer

    def get_queryset(self):
        team_id = self.kwargs['pk']
        unfinished_team_games = BasketballGame.objects.filter((Q(home__team__id=team_id) |
                                                               Q(away__team__id=team_id)) & Q(
            play_date__gte=timezone.now()))
        finished_team_games = BasketballGame.objects.filter((Q(home__team__id=team_id) |
                                                             Q(away__team__id=team_id)) & Q(
            play_date__lt=timezone.now()))
        return unfinished_team_games
