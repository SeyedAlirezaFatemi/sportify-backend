from django.db import models


class Person(models.Model):
    name = models.CharField()
    age = models.IntegerField(verbose_name='Age')
    positions = (
        'Coach',
        'Technical Personnel',
        'Defender',
        'Goalkeeper',
        'Forward',
        'Midfielder',
        'Shooting Guard',
        'Point Guard',
        'Center'
    )
    position = models.CharField(choices=positions)
    avatar = models.ImageField(verbose_name='Avatar')


class SoccerPlayer(Person):
    pass


class BasketballPlayer(Person):
    pass


class SoccerPlayerSeason(models.Model):
    player = models.ForeignKey(to=SoccerPlayer, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    reds = models.IntegerField(default=0)
    yellows = models.IntegerField(default=0)


class BasketballPlayerSeason(models.Model):
    player = models.ForeignKey(to=BasketballPlayer, on_delete=models.CASCADE)
    twos = models.IntegerField(default=0)
    threes = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    rebounds = models.IntegerField(default=0)
    fouls = models.IntegerField(default=0)
