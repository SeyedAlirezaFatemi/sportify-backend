from rest_framework import generics

from sport.models import SoccerPlayer
from sport.serializers import SoccerPlayerInfo


class SoccerPlayerDetail(generics.RetrieveAPIView):
    queryset = SoccerPlayer.objects.all()
    serializer_class = SoccerPlayerInfo
