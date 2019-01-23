from django.utils import timezone

from authentication.models import User
from news.models import News, Tag
from sport.models import BasketballPlayer, BasketballTeam, SoccerGame, SoccerGameTeamStatistic, SoccerPlayer, \
    SoccerPlayerSeason, SoccerTeam, SoccerEvent, League

# Times
now = timezone.now()
yesterday = now - timezone.timedelta(days=1)
tomorrow = now + timezone.timedelta(days=1)
days_ago_150 = now - timezone.timedelta(days=150)
days_ago_300 = now - timezone.timedelta(days=300)
days_ago_450 = now - timezone.timedelta(days=450)
days_ago_600 = now - timezone.timedelta(days=600)

# Tags
iran_tag = Tag(title='Iran')
iran_tag.save()
spain_tag = Tag(title='Spain')
spain_tag.save()
national_tag = Tag(title='National')
national_tag.save()
global_tag = Tag(title='Global')
global_tag.save()
tag_2019 = Tag(title='2019')
tag_2019.save()
tag_2018 = Tag(title='2018')
tag_2018.save()
tag_rain = Tag(title='Rain')
tag_rain.save()
lebron_tag = Tag(title='Lebron James')
lebron_tag.save()
barcelona_tag = Tag(title='Barcelona')
barcelona_tag.save()
lakers_tag = Tag(title='Lakers')
lakers_tag.save()
liverpool_tag = Tag(title='Liverpool')
liverpool_tag.save()
munich_tag = Tag(title='Munich')
munich_tag.save()
celtics_tag = Tag(title='Celtics')
celtics_tag.save()

# Soccer Teams
barcelona = SoccerTeam(name='Barcelona')
barcelona.save()

chelsea = SoccerTeam(name='Chelsea')
chelsea.save()

liverpool = SoccerTeam(name='Liverpool')
liverpool.save()

madrid = SoccerTeam(name='Madrid')
madrid.save()

munich = SoccerTeam(name='Munich')
munich.save()

juventus = SoccerTeam(name='Juventus')
juventus.save()

# Basketball Teams
lakers = BasketballTeam(name='Lakers')
lakers.save()

celtics = BasketballTeam(name='Celtics')
celtics.save()

bucks = BasketballTeam(name='Bucks')
bucks.save()

wizards = BasketballTeam(name='Wizards')
wizards.save()

hornets = BasketballTeam(name='Hornets')
hornets.save()

jazz = BasketballTeam(name='Jazz')
jazz.save()

bulls = BasketballTeam(name='Bulls')
bulls.save()

nets = BasketballTeam(name='Nets')
nets.save()

suns = BasketballTeam(name='Suns')
suns.save()

magic = BasketballTeam(name='Magic')
magic.save()

pacers = BasketballTeam(name='Pacers')
pacers.save()

# Soccer Players
ahmad = SoccerPlayer(team=barcelona, name='Ahmad', age=24, nationality='Iran', position='Defender')
ahmad.save()

ahmad_season_1 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_150,
                                    end=now, goals=10, assists=2, reds=0, yellows=1)
ahmad_season_1.save()

ahmad_season_2 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_300,
                                    end=days_ago_150, goals=7, assists=3, reds=1, yellows=3)
ahmad_season_2.save()

ahmad_season_3 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_450,
                                    end=days_ago_300, goals=10, assists=6, reds=2, yellows=5)
ahmad_season_3.save()

ahmad_season_4 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_600,
                                    end=days_ago_450, goals=3, assists=2, reds=1, yellows=3)
ahmad_season_4.save()

reza = SoccerPlayer(team=barcelona, name='Reza', age=24, nationality='Iran', position='Defender')
reza.save()

reza_season_1 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_150,
                                   end=now, goals=10, assists=2, reds=0, yellows=1)
reza_season_1.save()

reza_season_2 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_300,
                                   end=days_ago_150, goals=7, assists=3, reds=1, yellows=3)
reza_season_2.save()

reza_season_3 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_450,
                                   end=days_ago_300, goals=10, assists=6, reds=2, yellows=5)
reza_season_3.save()

reza_season_4 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_600,
                                   end=days_ago_450, goals=3, assists=2, reds=1, yellows=3)
reza_season_4.save()

# Basketball Players
lebron = BasketballPlayer(team=lakers, name='Lebron James', age=33, nationality='American', position='Shooting Guard')
lebron.save()

# Games
home1 = SoccerGameTeamStatistic(team=barcelona, corners=12, fouls=2, goal_attempts=8, goals=2, possession=12.12)
home1.save()

away1 = SoccerGameTeamStatistic(team=madrid, corners=13, fouls=4, goal_attempts=9, goals=3, possession=65.12)
away1.save()

game1 = SoccerGame(home=home1, away=away1, play_date=timezone.now(), best_player=ahmad)
game1.save()

event1 = SoccerEvent(event_time=timezone.now() + timezone.timedelta(minutes=5), game_id=game1.id, event_type='RC')
event1.save()

event2 = SoccerEvent(event_time=timezone.now() + timezone.timedelta(minutes=7), game_id=game1.id, event_type='YC')
event2.save()

event3 = SoccerEvent(event_time=timezone.now() + timezone.timedelta(minutes=9), game_id=game1.id, event_type='GL')
event3.save()

event4 = SoccerEvent(event_time=timezone.now() + timezone.timedelta(minutes=13), game_id=game1.id, event_type='AT')
event4.save()

event5 = SoccerEvent(event_time=timezone.now() + timezone.timedelta(minutes=16), game_id=game1.id, event_type='PY')
event5.save()

event6 = SoccerEvent(event_time=timezone.now() + timezone.timedelta(minutes=34), game_id=game1.id, event_type='SN')
event6.save()


# News
test_user = User.objects.get(pk=1)

news1 = News(author=test_user, title='Big Explosion',
             text="""The official told CNN that Trump's idea is to put something on the table to get Democrats to engage with negotiations.
             Trump is not expected to back down from his demand for a border wall, but the plan will seek to entice Democrats by offering other concessions.
             """
             , pub_date=timezone.now())
news1.save()
news1.tags.add(iran_tag, spain_tag, national_tag)

news2 = News(author=test_user, title="Jones 'fit and ready' to face Rangers",
             text="""Kilmarnock manager Steve Clarke insists he will have no hesitation in playing Jordan Jones against Rangers on Wednesday.
             The 24-year-old winger signed a pre-contract agreement with Killie's title rivals last week and will join Rangers on a four-year contract in the summer.
             """
             , pub_date=timezone.now(),
             brief="Kilmarnock manager Steve Clarke insists he will have no hesitation in playing Jordan Jones against Rangers on Wednesday.")
news2.save()
news2.tags.add(national_tag, global_tag, tag_2019)

# Leagues
league_1 = League(name="LaLiga", beginning_year=2018, end_year=2019)
league_2 = League(name="LaLiga2", beginning_year=2017, end_year=2018)
league_3 = League(name="LaLiga3", beginning_year=2016, end_year=2017)
league_4 = League(name="LaLiga4", beginning_year=2015, end_year=2016)
league_5 = League(name="LaLiga5", beginning_year=2014, end_year=2015)
league_6 = League(name="LaLiga6", beginning_year=2013, end_year=2014)
league_7 = League(name="LaLiga7", beginning_year=2012, end_year=2013)
league_8 = League(name="LaLiga8", beginning_year=2011, end_year=2012)
league_1.save()
league_2.save()
league_3.save()
league_4.save()
league_5.save()
league_6.save()
league_7.save()
league_8.save()
