from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(verbose_name='Age')
    nationality = models.CharField(max_length=100, default='Iran')
    positions = (
        ('CH', 'Coach'),
        ('TP', 'Technical Personnel'),
        ('DR', 'Defender'),
        ('GR', 'Goalkeeper'),
        ('FD', 'Forward'),
        ('M', 'Midfielder'),
        ('SG', 'Shooting Guard'),
        ('PG', 'Point Guard'),
        ('CR', 'Center'),
    )
    position = models.CharField(max_length=100, choices=positions)
    avatar = models.ImageField(verbose_name='Avatar')
    sports = (
        ('N', 'None'),
        ('S', 'Soccer'),
        ('B', 'Basketball'),
    )
    sport = models.CharField(max_length=10, choices=sports, default='Soccer')


class SoccerPlayer(Person):
    team = models.ForeignKey(to='SoccerTeam', on_delete=models.SET_NULL, null=True)


class SoccerPlayerImage(models.Model):
    player = models.ForeignKey(to=SoccerPlayer, related_name='images', on_delete=models.CASCADE)
    address = models.CharField(max_length=1000, null=True)
    image = models.ImageField()


class BasketballPlayer(Person):
    team = models.ForeignKey(to='BasketballTeam', on_delete=models.SET_NULL, null=True)


class BasketballPlayerImage(models.Model):
    player = models.ForeignKey(to=BasketballPlayer, related_name='images', on_delete=models.CASCADE)
    address = models.CharField(max_length=1000, null=True)
    image = models.ImageField()


class Season(models.Model):
    beginning = models.DateField()
    end = models.DateField()

    class Meta:
        abstract = True


class SoccerPlayerSeason(Season):
    player = models.ForeignKey(to=SoccerPlayer, related_name='seasons', on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    reds = models.IntegerField(default=0)
    yellows = models.IntegerField(default=0)


class BasketballPlayerSeason(Season):
    player = models.ForeignKey(to=BasketballPlayer, related_name='seasons', on_delete=models.CASCADE)
    twos = models.IntegerField(default=0)
    threes = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    rebounds = models.IntegerField(default=0)
    fouls = models.IntegerField(default=0)


class League(models.Model):
    name = models.CharField(max_length=100)
    sports = (
        ('N', 'None'),
        ('S', 'Soccer'),
        ('B', 'Basketball'),
    )
    sport = models.CharField(max_length=20, choices=sports, default='Soccer')
    country = models.CharField(max_length=50, default='Iran')
    status = models.BooleanField(default=True)
    beginning_year = models.IntegerField()
    end_year = models.IntegerField()


class Game(models.Model):
    play_date = models.DateTimeField()
    league = models.ForeignKey(to=League, on_delete=models.SET_NULL, null=True)
    home_score = models.IntegerField(default=-1)
    away_score = models.IntegerField(default=-1)

    class Meta:
        abstract = True


class Team(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class SoccerTeam(Team):
    pass


class BasketballTeam(Team):
    pass


class SoccerTeamImage(models.Model):
    team = models.ForeignKey(to=SoccerTeam, related_name='images', on_delete=models.CASCADE)
    address = models.CharField(max_length=1000, null=True)
    image = models.ImageField(null=True)


class BasketballTeamImage(models.Model):
    team = models.ForeignKey(to=BasketballTeam, related_name='images', on_delete=models.CASCADE)
    address = models.CharField(max_length=1000, null=True)
    image = models.ImageField(null=True)


class SoccerGameTeamStatistic(models.Model):
    team = models.ForeignKey(to=SoccerTeam, on_delete=models.CASCADE)
    possession = models.IntegerField(default=0)
    shots_on_target = models.IntegerField(default=0)
    fouls_offside = models.IntegerField(default=0)
    corner_kicks = models.IntegerField(default=0)
    passes = models.IntegerField(default=0)
    crosses = models.IntegerField(default=0)
    interceptions = models.IntegerField(default=0)
    tackles = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)


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


class SoccerGame(Game):
    home = models.OneToOneField(to=SoccerGameTeamStatistic, related_name='home', on_delete=models.CASCADE)
    away = models.OneToOneField(to=SoccerGameTeamStatistic, related_name='away', on_delete=models.CASCADE)
    starters = models.ManyToManyField(to=SoccerPlayer, related_name='starters')
    bench = models.ManyToManyField(to=SoccerPlayer, related_name='benchs')
    best_player = models.ForeignKey(to=SoccerPlayer, related_name='bests', on_delete=models.SET_NULL, null=True)


class BasketballGame(Game):
    home = models.OneToOneField(to=BasketballGameTeamStatistic, related_name='home', on_delete=models.CASCADE)
    away = models.OneToOneField(to=BasketballGameTeamStatistic, related_name='away', on_delete=models.CASCADE)
    starters = models.ManyToManyField(to=BasketballPlayer, related_name='starters')
    bench = models.ManyToManyField(to=BasketballPlayer, related_name='benchs')


class SoccerGameImage(models.Model):
    game = models.ForeignKey(to=SoccerGame, related_name='images', on_delete=models.CASCADE)
    address = models.CharField(max_length=1000, null=True)
    image = models.ImageField()


class BasketballGameImage(models.Model):
    image = models.ImageField()
    address = models.CharField(max_length=1000, null=True)
    game = models.ForeignKey(to=BasketballGame, related_name='images', on_delete=models.CASCADE)


class SoccerEvent(models.Model):
    event_time = models.TimeField(verbose_name='Time')
    events = (
        ('RC', 'Red Card'),
        ('YC', 'Yellow Card'),
        ('GL', 'Goal'),
        ('AT', 'Assist'),
        ('PY', 'Penalty'),
        ('SNI', 'Substitution in'),
        ('SNO', 'Substitution out'),
    )
    event_type = models.CharField(max_length=100, choices=events)
    game = models.ForeignKey(to=SoccerGame, on_delete=models.CASCADE)


class BasketballEvent(models.Model):
    event_time = models.TimeField(verbose_name='Time')
    events = (
        ('AT', 'Assist'),
        ('PY', 'Penalty'),
        ('SN', 'Substitution'),
        ('2P', '2 Point'),
        ('3P', '3 Point'),
        ('FT', 'Free Throw'),
        ('RD', 'Rebound'),
    )
    event_type = models.CharField(max_length=100, choices=events)
    game = models.ForeignKey(to=BasketballGame, on_delete=models.CASCADE)


class BasketballPlayerGameStatistics(models.Model):
    game = models.ForeignKey(to=BasketballGame, on_delete=models.CASCADE)
    player = models.ForeignKey(to=BasketballPlayer, on_delete=models.CASCADE)
    twos = models.IntegerField(default=0)
    threes = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    rebounds = models.IntegerField(default=0)
    fouls = models.IntegerField(default=0)


class SoccerTeamLeagueStatistic(models.Model):
    league = models.ForeignKey(to=League, on_delete=models.CASCADE)
    team = models.ForeignKey(to=SoccerTeam, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
    games = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    goal_difference = models.IntegerField(default=0)
    score = models.IntegerField(default=0)


class BasketballTeamLeagueStatistic(models.Model):
    league = models.ForeignKey(to=League, on_delete=models.CASCADE)
    team = models.ForeignKey(to=BasketballTeam, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
    games = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    percentage = models.FloatField(default=0)
