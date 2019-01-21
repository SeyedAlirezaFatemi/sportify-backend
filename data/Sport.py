from django.utils import timezone

from sport.models import SoccerGame, SoccerGameTeamStatistic, SoccerPlayer, SoccerTeam

peikan = SoccerTeam(name='Peikan')
peikan.save()

ahmad = SoccerPlayer(team=peikan, name='Ahmad', age=24, nationality='Iran', position='Defender')
ahmad.save()

home1 = SoccerGameTeamStatistic(team=peikan, corners=12, fouls=12, goal_attempts=12, goals=12, possession=12.12)
home1.save()

away1 = SoccerGameTeamStatistic(team=peikan, corners=12, fouls=12, goal_attempts=12, goals=12, possession=12.12)
away1.save()

game1 = SoccerGame(home=home1, away=away1, play_date=timezone.now(), best_player=ahmad)
game1.save()
