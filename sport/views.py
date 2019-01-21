from rest_framework import generics

from sport.models import *
from sport.serializers.player_serializer import *


class BasketballPlayerStatistics(generics.RetrieveAPIView):
    model = BasketballPlayer
    serializer_class = BasketballPlayerSerializer

    def get_queryset(self):
        queryset = BasketballPlayer.objects.all()
        player_id = self.request.query_params.get('player_id')

        return queryset.get(id=player_id)


class SoccerPlayerStatistics(generics.RetrieveAPIView):
    model = SoccerPlayer
    serializer_class = SoccerPlayerSerializer

    def get_queryset(self):
        queryset = SoccerPlayer.objects.all()
        player_id = self.request.query_params.get('player_id')

        return queryset.get(id=player_id)


class SoccerPlayerDetail(generics.RetrieveAPIView):
    queryset = SoccerPlayer.objects.all()
    # serializer_class = SoccerPlayerInfo
