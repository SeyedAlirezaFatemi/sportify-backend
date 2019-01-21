from django.utils import timezone

from sport.models import SoccerGame, SoccerGameTeamStatistic, SoccerTeam

team1 = SoccerTeam(name='barcelona')
team2 = SoccerTeam(name='real madrid')
team1.save()
team2.save()
sgts1 = SoccerGameTeamStatistic(team=team1)
sgts2 = SoccerGameTeamStatistic(team=team2)
sgts1.save()
sgts2.save()
game = SoccerGame(home=sgts1, away=sgts2, play_date=timezone.now() + timezone.timedelta(days=2))
game.save()
