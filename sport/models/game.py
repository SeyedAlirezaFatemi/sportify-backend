from django.db import models

from sport.models.people import BasketballPlayer, SoccerPlayer


class Game(models.Model):
    play_date = models.DateTimeField()

    # duration = models.TimeField()

    class Meta:
        abstract = True


class Team(models.Model):
    name = models.CharField()

    class Meta:
        abstract = True


class SoccerTeam(Team):
    pass


class BasketballTeam(Team):
    pass


class SoccerGameTeamStatistic(models.Model):
    team = models.ForeignKey(to=SoccerTeam, on_delete=models.CASCADE)
    corners = models.IntegerField(default=0)
    fouls = models.IntegerField(default=0)
    goal_attempts = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    possession = models.FloatField(default=0.0)


class BasketballGameTeamStatistic(models.Model):
    team = models.ForeignKey(to=BasketballTeam, on_delete=models.CASCADE)
    twos = models.IntegerField(default=0)
    threes = models.IntegerField(default=0)
    fouls = models.IntegerField(default=0)
    free_throws = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    first_quarter_points = models.IntegerField(default=0)
    second_quarter_points = models.IntegerField(default=0)
    third_quarter_points = models.IntegerField(default=0)
    fourth_quarter_points = models.IntegerField(default=0)


class Event(models.Model):
    event_time = models.TimeField(verbose_name='Time')
    events = (
        'Red Card',
        'Yellow Card',
        'Goal',
        'Assist',
        'Penalty',
        'Substitution',
        '2 Point',
        '3 Point',
        'Free Throw',
        'Rebound',
    )
    event_type = models.CharField(choices=events)
    game = models.ForeignKey(to=Game, on_delete=models.CASCADE)


class BasketballPlayerGameStatistics(models.Model):
    game = models.ForeignKey(to=Game, on_delete=models.CASCADE)
    player = models.ForeignKey(to=BasketballPlayer, on_delete=models.CASCADE)
    twos = models.IntegerField(default=0)
    threes = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    rebounds = models.IntegerField(default=0)
    fouls = models.IntegerField(default=0)


class GameImage(models.Model):
    image = models.ImageField()
    game = models.ForeignKey(to=Game, on_delete=models.CASCADE)


class SoccerGame(Game):
    home = models.OneToOneField(to=SoccerGameTeamStatistic, on_delete=models.CASCADE)
    away = models.OneToOneField(to=SoccerGameTeamStatistic, on_delete=models.CASCADE)
    starters = models.ManyToManyField(to=SoccerPlayer)
    bench = models.ManyToManyField(to=SoccerPlayer)
    best_player = models.ForeignKey(to=SoccerPlayer, on_delete=models.SET_NULL)


class BasketballGame(Game):
    home = models.OneToOneField(to=BasketballGameTeamStatistic, on_delete=models.CASCADE)
    away = models.OneToOneField(to=BasketballGameTeamStatistic, on_delete=models.CASCADE)
    starters = models.ManyToManyField(to=BasketballPlayer)
    bench = models.ManyToManyField(to=BasketballPlayer)
