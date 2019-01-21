from rest_framework import generics

from sport.models import BasketballPlayerSeason, SoccerPlayerSeason
from sport.serializers.player_serializer import BasketballPlayerSeasonSerializer, SoccerPlayerSeasonSerializer


class BasketballPlayerStatistics(generics.RetrieveAPIView):
    serializer_class = BasketballPlayerSeasonSerializer
    queryset = BasketballPlayerSeason.objects.all()


class SoccerPlayerStatistics(generics.RetrieveAPIView):
    queryset = SoccerPlayerSeason.objects.all()
    serializer_class = SoccerPlayerSeasonSerializer
