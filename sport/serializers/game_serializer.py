from rest_framework.serializers import ModelSerializer

from sport.models import BasketballGame, BasketballGameImage, BasketballGameTeamStatistic, \
    BasketballPlayerGameStatistics, BasketballTeam, Game, SoccerGame, SoccerGameImage, SoccerGameTeamStatistic, \
    SoccerTeam, Team


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


class SoccerGameImageSerializer(ModelSerializer):
    class Meta:
        model = SoccerGameImage
        fields = "__all__"
        depth = 1


class BasketballGameImageSerializer(ModelSerializer):
    class Meta:
        model = BasketballGameImage
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
