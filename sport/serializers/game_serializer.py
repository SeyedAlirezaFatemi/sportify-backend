from rest_framework.serializers import ModelSerializer, SerializerMethodField

from sport.models import BasketballEvent, BasketballGame, BasketballGameImage, BasketballGameTeamStatistic, \
    BasketballPlayerGameStatistics, BasketballTeam, Game, League, SoccerEvent, SoccerGame, SoccerGameImage, \
    SoccerGameTeamStatistic, SoccerTeam, Team


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        depth = 1


class SoccerGameTeamStatisticSerializer(ModelSerializer):
    class Meta:
        model = SoccerGameTeamStatistic
        fields = '__all__'
        depth = 1


class BasketballGameTeamStatisticSerializer(ModelSerializer):
    class Meta:
        model = BasketballGameTeamStatistic
        fields = '__all__'
        depth = 1


class BasketballPlayerGameStatisticsSerializer(ModelSerializer):
    class Meta:
        model = BasketballPlayerGameStatistics
        fields = '__all__'
        depth = 1


class SoccerGameImageSerializer(ModelSerializer):
    class Meta:
        model = SoccerGameImage
        fields = '__all__'


class BasketballGameImageSerializer(ModelSerializer):
    class Meta:
        model = BasketballGameImage
        fields = '__all__'


class SoccerGameSerializer(ModelSerializer):
    class Meta:
        model = SoccerGame
        fields = '__all__'
        depth = 1


class SoccerGameStatisticsSerializer(ModelSerializer):
    class Meta:
        model = SoccerGame
        fields = ('home', 'away',)
        depth = 1


class BasketballGameStatisticsSerializer(ModelSerializer):
    class Meta:
        model = BasketballGame
        fields = ('home', 'away',)
        depth = 1


class BasketballGameSerializer(ModelSerializer):
    class Meta:
        model = BasketballGame
        fields = '__all__'
        depth = 1


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        depth = 1


class SoccerTeamSerializer(ModelSerializer):
    class Meta:
        model = SoccerTeam
        fields = '__all__'
        depth = 1


class BasketballTeamSerializer(ModelSerializer):
    class Meta:
        model = BasketballTeam
        fields = '__all__'
        depth = 1


class LeagueSerializer(ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'
        depth = 1


class SoccerImagesSerializer(ModelSerializer):
    class Meta:
        model = SoccerGame
        fields = ('image',)
        depth = 1


class BasketballImagesSerializer(ModelSerializer):
    class Meta:
        model = BasketballGame
        fields = ('image',)
        depth = 1


class SoccerEventSerializer(ModelSerializer):
    event_type = SerializerMethodField()

    def get_event_type(self, obj):
        print(obj.__dict__)
        return obj.get_event_type_display()

    class Meta:
        model = SoccerEvent
        fields = ('event_time', 'event_type')
        depth = 1


class BasketballEventSerializer(ModelSerializer):
    event_type = SerializerMethodField()

    def get_event_type(self, obj):
        return obj.get_event_type_display()

    class Meta:
        model = BasketballEvent
        fields = ('event_time', 'event_type')
        depth = 1
