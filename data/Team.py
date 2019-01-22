from django.utils import timezone

from authentication.models import User
from news.models import News
from sport.models import SoccerTeam, SoccerTeamImage

team1 = SoccerTeam(name='Bayern')
team1.save()
user1 = User.objects.get(pk=1)
user1.save()

news_3 = News(author=user1, title='I am happy in la', brief='This is Stupid! '
              , text='Lebron James went home. Nobody really cares about him. He died peacefully.',
              pub_date=timezone.now())
news_3.save()

team_image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/FC_Bayern_M%C3%BCnchen_logo_%282017%29.svg/220px-FC_Bayern_M%C3%BCnchen_logo_%282017%29.svg.png'

soccer_team_image = SoccerTeamImage(team=team1, address=team_image_url)
soccer_team_image.save()
