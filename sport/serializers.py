from rest_framework.serializers import ModelSerializer

from sport.models import SoccerPlayer


class SoccerPlayerInfo(ModelSerializer):
    class Meta:
        model = SoccerPlayer
        fields = ('name', 'age', 'nationality', 'position', 'avatar', 'team')
