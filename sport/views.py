
from rest_framework import generics

from .models.people import *
from .serializers.player_serializer import *


class BasketballPlayerStatistics(generics.RetrieveAPIView):
    model = BasketballPlayer
    serializer_class = BasketballPlayerSeasonSerializer

    def get_queryset(self):
        queryset = BasketballPlayer.objects.all()
        player_id = self.request.query_params.get('player_id')

        return queryset.get(id=player_id)

