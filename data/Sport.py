from django.utils import timezone

from authentication.models import User
from news.models import News, Tag
from sport.models import BasketballPlayer, BasketballTeam, SoccerGame, SoccerGameTeamStatistic, SoccerPlayer, \
    SoccerPlayerSeason, SoccerTeam

peikan = SoccerTeam(name='Peikan')
peikan.save()

ahmad = SoccerPlayer(team=peikan, name='Ahmad', age=24, nationality='Iran', position='Defender')
ahmad.save()

ahmad_season_1 = SoccerPlayerSeason(player=ahmad, beginning=timezone.now() - timezone.timedelta(days=150),
                                    end=timezone.now(), goals=10, assists=2, reds=0, yellows=1)
ahmad_season_1.save()

tag1 = Tag(title='Lebron')
tag2 = Tag(title='Lakers')
tag1.save()
tag2.save()

user1 = User.objects.get(pk=1)

news_1 = News(author=user1, title='Lebron James is happy in la', brief='sdsauhda hsjdhasudh ashdhan '
              , text='dasdnaskd uadkjas ndjn asjndkjasn dkj', pub_date=timezone.now())
news_1.save()

tag3 = Tag(title='Lebron James')
tag3.save()

news_2 = News(author=user1, title='I am happy in la', brief='sdsauhda hsjdhasudh ashdhan '
              , text='Lebron James uadkjas ndjn asjndkjasn dkj', pub_date=timezone.now())
news_2.save()
news_2.tags.add(tag1, tag3)

lakers = BasketballTeam(name='Lakers')
lakers.save()

lebron = BasketballPlayer(team=lakers, name='Lebron James', age=33, nationality='American', position='Shooting Guard')
lebron.save()

home1 = SoccerGameTeamStatistic(team=peikan, corners=12, fouls=12, goal_attempts=12, goals=12, possession=12.12)
home1.save()

away1 = SoccerGameTeamStatistic(team=peikan, corners=12, fouls=12, goal_attempts=12, goals=12, possession=12.12)
away1.save()

game1 = SoccerGame(home=home1, away=away1, play_date=timezone.now(), best_player=ahmad)
game1.save()
