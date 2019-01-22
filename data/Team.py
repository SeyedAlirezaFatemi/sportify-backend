from django.utils import timezone

from authentication.models import User
from news.models import News
from sport.models import SoccerTeam

team1 = SoccerTeam(name='Bayern')
team1.save()

user1 = User.objects.get(pk=1)
user1.save()

news_3 = News(author=user1, title='I am happy in la', brief='This is Stupid! '
              , text='Lebron James went home. Nobody really cares about him. He died peacefully.',
              pub_date=timezone.now())
news_3.save()
