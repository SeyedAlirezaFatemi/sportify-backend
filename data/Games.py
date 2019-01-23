from django.utils import timezone

from sport.models import SoccerGame, SoccerGameTeamStatistic, SoccerTeam

team1 = SoccerTeam(name='Barcelona')
team2 = SoccerTeam(name='Real Madrid')
team1.save()
team2.save()
sgts1 = SoccerGameTeamStatistic(team=team1, possession=5, shots_on_target=4, fouls_offside=12, corner_kicks=14,
                                passes=45, crosses=31, interceptions=25, tackles=7, saves=55)
sgts2 = SoccerGameTeamStatistic(team=team2, possession=6, shots_on_target=5, fouls_offside=13, corner_kicks=15,
                                passes=46, crosses=32, interceptions=26, tackles=8, saves=56)
sgts1.save()
sgts2.save()
game = SoccerGame(home=sgts1, away=sgts2, play_date=timezone.now() + timezone.timedelta(days=2))
game.save()
