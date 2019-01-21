from authentication.models import User
from news.models import News, Tag
from sport.models import SoccerPlayer, SoccerTeam, SoccerPlayerSeason, Person
from django.utils import timezone


peikan = SoccerTeam(name='Peikan')
peikan.save()

ahmad = SoccerPlayer(team=peikan, name='Ahmad', age=24, nationality='Iran', position='Defender')
ahmad.save()

ahmad_season_1 = SoccerPlayerSeason(player=ahmad, beginning=timezone.now() - timezone.timedelta(days=150), end=timezone.now(), goals=10, assists=2, reds=0, yellows=1)
ahmad_season_1.save()


tag1 = Tag(title='Lebron')
tag2 = Tag(title='Lakers')
tag1.save()
tag2.save()
user1 = User.objects.get(pk=1)
user1.save()
news_1 = News(author=user1, title='Lebron James is happy in la', brief='sdsauhda hsjdhasudh ashdhan '
              , text='dasdnaskd uadkjas ndjn asjndkjasn dkj', pub_date=timezone.now())
news_1.save()
tag3 = Tag(title='Lebron James')
tag3.save()
news_2 = News(author=user1, title='I am happy in la', brief='sdsauhda hsjdhasudh ashdhan '
              , text='Lebron James uadkjas ndjn asjndkjasn dkj', pub_date=timezone.now())
news_2.save()
news_2.tags.add(tag1, tag3)
lebron = Person(name='Lebron James', age=33, nationality='american', position='FD')
lebron.save()