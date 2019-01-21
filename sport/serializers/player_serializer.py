from rest_framework.serializers import ModelSerializer

from sport.models import BasketballPlayer, BasketballPlayerSeason, Person, Season, SoccerPlayer, SoccerPlayerSeason


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        depth = 1


class SoccerPlayerSerializer(ModelSerializer):
    class Meta:
        model = SoccerPlayer
        fields = "__all__"
        depth = 1


class BasketballPlayerSerializer(ModelSerializer):
    class Meta:
        model = BasketballPlayer
        fields = "__all__"
        depth = 1


class SeasonSerializer(ModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"
        depth = 1


class BasketballPlayerSeasonSerializer(ModelSerializer):
    class Meta:
        model = BasketballPlayerSeason
        fields = "__all__"
        depth = 1


class SoccerPlayerSeasonSerializer(ModelSerializer):
    class Meta:
        model = SoccerPlayerSeason
        fields = "__all__"
        depth = 1
