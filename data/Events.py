from django.utils import timezone

from sport.models import SoccerEvent, SoccerGame, SoccerGameTeamStatistic, SoccerTeam

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

event1 = SoccerEvent(event_time=timezone.now() + timezone.timedelta(minutes=5), game_id=game.id, event_type='RC')
event1.save()

event2 = SoccerEvent(event_time=timezone.now() + timezone.timedelta(minutes=7), game_id=game.id, event_type='YC')
event2.save()

event3 = SoccerEvent(event_time=timezone.now() + timezone.timedelta(minutes=9), game_id=game.id, event_type='GL')
event3.save()

event4 = SoccerEvent(event_time=timezone.now() + timezone.timedelta(minutes=13), game_id=game.id, event_type='AT')
event4.save()

event5 = SoccerEvent(event_time=timezone.now() + timezone.timedelta(minutes=16), game_id=game.id, event_type='PY')
event5.save()

event6 = SoccerEvent(event_time=timezone.now() + timezone.timedelta(minutes=34), game_id=game.id, event_type='SN')
event6.save()
