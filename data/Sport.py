from sport.models import SoccerPlayer, SoccerTeam

peikan = SoccerTeam(name='Peikan')
peikan.save()

ahmad = SoccerPlayer(team=peikan, name='Ahmad', age=24, nationality='Iran', position='Defender')
ahmad.save()
