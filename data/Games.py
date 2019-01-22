from django.utils import timezone

from sport.models import SoccerGame, SoccerGameTeamStatistic, SoccerTeam

team1 = SoccerTeam(name='Barcelona')
team2 = SoccerTeam(name='Real Madrid')
team1.save()
team2.save()
sgts1 = SoccerGameTeamStatistic(team=team1, corners=5, fouls=443, goal_attempts=12, goals=12, possession=45.12)
sgts2 = SoccerGameTeamStatistic(team=team2, corners=4, fouls=12, goal_attempts=12, goals=12, possession=90.12)
sgts1.save()
sgts2.save()
game = SoccerGame(home=sgts1, away=sgts2, play_date=timezone.now() + timezone.timedelta(days=2))
game.save()
