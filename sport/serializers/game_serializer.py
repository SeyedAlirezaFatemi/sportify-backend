from rest_framework.serializers import ModelSerializer

from sport.models.game import *


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
        depth = 1


class SoccerGameTeamStatisticSerializer(ModelSerializer):
    class Meta:
        model = SoccerGameTeamStatistic
        fields = "__all__"
        depth = 1


class BasketballGameTeamStatisticSerializer(ModelSerializer):
    class Meta:
        model = BasketballGameTeamStatistic
        fields = "__all__"
        depth = 1


class BasketballPlayerGameStatisticsSerializer(ModelSerializer):
    class Meta:
        model = BasketballPlayerGameStatistics
        fields = "__all__"
        depth = 1


class GameImageSerializer(ModelSerializer):
    class Meta:
        model = GameImage
        fields = "__all__"
        depth = 1


class SoccerGameSerializer(ModelSerializer):
    class Meta:
        model = SoccerGame
        fields = "__all__"
        depth = 1


class BasketballGameSerializer(ModelSerializer):
    class Meta:
        model = BasketballGame
        fields = "__all__"
        depth = 1


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
        depth = 1


class SoccerTeamSerializer(ModelSerializer):
    class Meta:
        model = SoccerTeam
        fields = "__all__"
        depth = 1


class BasketballTeamSerializer(ModelSerializer):
    class Meta:
        model = BasketballTeam
        fields = "__all__"
        depth = 1