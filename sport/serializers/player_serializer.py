from rest_framework.serializers import ModelSerializer, SerializerMethodField

from sport.models import BasketballPlayer, BasketballPlayerSeason, Person, Season, SoccerPlayer, SoccerPlayerSeason


class PersonSerializer(ModelSerializer):
    sport = SerializerMethodField()

    def get_sport(self, obj):
        return obj.get_sport_display()

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


class SoccerPlayerImagesSerializer(ModelSerializer):
    class Meta:
        model = SoccerPlayer
        fields = ('images',)
        depth = 1


class BasketballPlayerImagesSerializer(ModelSerializer):
    class Meta:
        model = BasketballPlayer
        fields = ('images',)
        depth = 1


class BasketballPlayerStatisticsSerializer(ModelSerializer):
    class Meta:
        model = BasketballPlayer
        fields = ('seasons',)
        depth = 1


class SoccerPlayerStatisticsSerializer(ModelSerializer):
    class Meta:
        model = SoccerPlayer
        fields = ('seasons',)
        depth = 1
