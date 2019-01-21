from django.db.models import Q
from rest_framework import generics

from sport.models import BasketballGame, BasketballPlayer, SoccerGame, SoccerPlayer
from sport.serializers.game_serializer import BasketballImagesSerializer, SoccerImagesSerializer
from sport.models import *
from news.models import News
from sport.serializers.player_serializer import *
from news.serializers import NewsSerializer
from sport.models import SoccerPlayer
from sport.serializers.player_serializer import BasketballPlayerSeason, BasketballPlayerSeasonSerializer, \
    BasketballPlayerSerializer, SoccerPlayerSeason, SoccerPlayerSeasonSerializer, SoccerPlayerSerializer


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
