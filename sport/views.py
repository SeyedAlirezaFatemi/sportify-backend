from rest_framework import generics

from sport.models import BasketballPlayer, SoccerPlayer
from sport.serializers.player_serializer import BasketballPlayerSeason, BasketballPlayerSeasonSerializer, \
    BasketballPlayerSerializer, SoccerPlayerSeason, SoccerPlayerSeasonSerializer, SoccerPlayerSerializer


class BasketballPlayerStatistics(generics.RetrieveAPIView):
    serializer_class = BasketballPlayerSeasonSerializer
    queryset = BasketballPlayerSeason.objects.all()


class SoccerPlayerStatistics(generics.RetrieveAPIView):
    queryset = SoccerPlayerSeason.objects.all()
    serializer_class = SoccerPlayerSeasonSerializer


class SoccerPlayerInfo(generics.RetrieveAPIView):
    queryset = SoccerPlayer.objects.all()
    serializer_class = SoccerPlayerSerializer


class BasketballPlayerInfo(generics.RetrieveAPIView):
    queryset = BasketballPlayer.objects.all()
    serializer_class = BasketballPlayerSerializer
