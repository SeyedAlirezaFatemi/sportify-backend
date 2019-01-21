from rest_framework import generics

from sport.serializers.player_serializer import BasketballPlayerSeason, BasketballPlayerSeasonSerializer, \
    SoccerPlayerSeason, SoccerPlayerSeasonSerializer


class BasketballPlayerStatistics(generics.RetrieveAPIView):
    serializer_class = BasketballPlayerSeasonSerializer
    queryset = BasketballPlayerSeason.objects.all()


class SoccerPlayerStatistics(generics.RetrieveAPIView):
    queryset = SoccerPlayerSeason.objects.all()
    serializer_class = SoccerPlayerSeasonSerializer
