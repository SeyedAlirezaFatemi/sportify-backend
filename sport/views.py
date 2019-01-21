
from rest_framework import generics

from .models.people import *
from .serializers.player_serializer import *


class BasketballPlayerStatistics(generics.RetrieveAPIView):
    serializer_class = BasketballPlayerSerializer
    queryset = BasketballPlayer.objects.all()


class SoccerPlayerStatistics(generics.RetrieveAPIView):
    queryset = SoccerPlayer.objects.all()
    serializer_class = SoccerPlayerSerializer
