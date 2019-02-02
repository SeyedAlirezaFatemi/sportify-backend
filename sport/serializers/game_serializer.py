from rest_framework.serializers import ModelSerializer, SerializerMethodField

from sport.models import *


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
        depth = 2


class SoccerGameStatisticsSerializer(ModelSerializer):
    class Meta:
        model = SoccerGame
        fields = ('home', 'away',)
        depth = 2


class BasketballGameStatisticsSerializer(ModelSerializer):
    class Meta:
        model = BasketballGame
        fields = ('home', 'away',)
        depth = 2


class BasketballGameSerializer(ModelSerializer):
    class Meta:
        model = BasketballGame
        fields = '__all__'
        depth = 2


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
        fields = ('images',)
        depth = 1


class BasketballImagesSerializer(ModelSerializer):
    class Meta:
        model = BasketballGame
        fields = ('images',)
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


class SoccerTeamImageSerializer(ModelSerializer):
    class Meta:
        model = SoccerTeamImage
        fields = ('address', 'image')
        depth = 1


class BasketballTeamImageSerializer(ModelSerializer):
    class Meta:
        model = BasketballTeamImage
        fields = ('address', 'image')
        depth = 1


class SoccerTeamImagesSerializer(ModelSerializer):
    class Meta:
        model = SoccerTeam
        fields = ('images',)
        depth = 1


class BasketballTeamImagesSerializer(ModelSerializer):
    class Meta:
        model = BasketballTeam
        fields = ('images',)
        depth = 1


class BasketballTeamLeagueStatisticSerializer(ModelSerializer):
    class Meta:
        model = BasketballTeamLeagueStatistic
        fields = '__all__'
        depth = 1


class SoccerTeamLeagueStatisticSerializer(ModelSerializer):
    class Meta:
        model = SoccerTeamLeagueStatistic
        fields = '__all__'
        depth = 1


class SoccerTeamVideoSerializer(ModelSerializer):
    class Meta:
        model = SoccerTeamVideo
        fields = '__all__'
        depth = 1


class BasketballTeamVideoSerializer(ModelSerializer):
    class Meta:
        model = BasketballTeamVideo
        fields = '__all__'
        depth = 1


class BasketballGameVideoSerializer(ModelSerializer):
    class Meta:
        model = BasketballGameVideo
        fields = '__all__'
        depth = 1


class SoccerGameVideoSerializer(ModelSerializer):
    class Meta:
        model = SoccerGameVideo
        fields = '__all__'
        depth = 1


class PlayerVideoSerializer(ModelSerializer):
    class Meta:
        model = PlayerVideo
        fields = '__all__'
        depth = 1
