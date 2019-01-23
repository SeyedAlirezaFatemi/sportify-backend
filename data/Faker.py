from django.utils import timezone

from authentication.models import User
from news.models import News, Tag
from sport.models import BasketballEvent, BasketballGame, BasketballGameTeamStatistic, BasketballPlayer, \
    BasketballPlayerSeason, BasketballTeam, BasketballTeamLeagueStatistic, League, SoccerEvent, SoccerGame, \
    SoccerGameTeamStatistic, SoccerPlayer, SoccerPlayerSeason, SoccerTeam, SoccerTeamLeagueStatistic

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

ahmad_season_1 = SoccerPlayerSeason(player=ahmad, beginning=now,
                                    end=days_ago_150, goals=10, assists=2, reds=0, yellows=1)
ahmad_season_1.save()

ahmad_season_2 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_150,
                                    end=days_ago_300, goals=7, assists=3, reds=1, yellows=3)
ahmad_season_2.save()

ahmad_season_3 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_300,
                                    end=days_ago_450, goals=10, assists=6, reds=2, yellows=5)
ahmad_season_3.save()

ahmad_season_4 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_450,
                                    end=days_ago_600, goals=3, assists=2, reds=1, yellows=3)
ahmad_season_4.save()

reza = SoccerPlayer(team=barcelona, name='Reza', age=24, nationality='Iran', position='Defender')
reza.save()

reza_season_1 = SoccerPlayerSeason(player=ahmad, beginning=now,
                                   end=days_ago_150, goals=10, assists=2, reds=0, yellows=1)
reza_season_1.save()

reza_season_2 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_150,
                                   end=days_ago_300, goals=7, assists=3, reds=1, yellows=3)
reza_season_2.save()

reza_season_3 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_300,
                                   end=days_ago_450, goals=10, assists=6, reds=2, yellows=5)
reza_season_3.save()

reza_season_4 = SoccerPlayerSeason(player=ahmad, beginning=days_ago_450,
                                   end=days_ago_600, goals=3, assists=2, reds=1, yellows=3)
reza_season_4.save()
# Basketball Players
lebron = BasketballPlayer(team=lakers, name='Lebron James', age=33, nationality='American', position='Shooting Guard')
lebron.save()

jordan = BasketballPlayer(team=jazz, name='Michael Jordan', age=33, nationality='American', position='Shooting Guard')
jordan.save()

harden = BasketballPlayer(team=magic, name='James Harden', age=34, nationality='Afghanestan', position='Defending')
harden.save()
##########
lebron_season_1 = BasketballPlayerSeason(player=lebron, beginning=now, end=days_ago_150, twos=12, threes=20,
                                         minutes_played=769, rebounds=12, fouls=34)
lebron_season_1.save()

lebron_season_2 = BasketballPlayerSeason(player=lebron, beginning=days_ago_150, end=days_ago_300, twos=12, threes=20,
                                         minutes_played=769, rebounds=12, fouls=34)
lebron_season_2.save()

lebron_season_3 = BasketballPlayerSeason(player=lebron, beginning=days_ago_300, end=days_ago_450, twos=12, threes=20,
                                         minutes_played=769, rebounds=12, fouls=34)
lebron_season_3.save()

lebron_season_4 = BasketballPlayerSeason(player=lebron, beginning=days_ago_450, end=days_ago_600, twos=12, threes=20,
                                         minutes_played=769, rebounds=12, fouls=34)
lebron_season_4.save()
##########
harden_season_1 = BasketballPlayerSeason(player=harden, beginning=now, end=days_ago_150, twos=12, threes=20,
                                         minutes_played=769, rebounds=12, fouls=34)
harden_season_1.save()

harden_season_2 = BasketballPlayerSeason(player=harden, beginning=days_ago_150, end=days_ago_300, twos=12, threes=20,
                                         minutes_played=769, rebounds=12, fouls=34)
harden_season_2.save()

harden_season_3 = BasketballPlayerSeason(player=harden, beginning=days_ago_300, end=days_ago_450, twos=12, threes=20,
                                         minutes_played=769, rebounds=12, fouls=34)
harden_season_3.save()

harden_season_4 = BasketballPlayerSeason(player=harden, beginning=days_ago_450, end=days_ago_600, twos=12, threes=20,
                                         minutes_played=769, rebounds=12, fouls=34)
harden_season_4.save()
##########
jordan_season_1 = BasketballPlayerSeason(player=jordan, beginning=now, end=days_ago_150, twos=12, threes=20,
                                         minutes_played=769, rebounds=12, fouls=34)
jordan_season_1.save()

jordan_season_2 = BasketballPlayerSeason(player=jordan, beginning=days_ago_150, end=days_ago_300, twos=12, threes=20,
                                         minutes_played=769, rebounds=12, fouls=34)
jordan_season_2.save()

jordan_season_3 = BasketballPlayerSeason(player=jordan, beginning=days_ago_300, end=days_ago_450, twos=12, threes=20,
                                         minutes_played=769, rebounds=12, fouls=34)
jordan_season_3.save()

jordan_season_4 = BasketballPlayerSeason(player=jordan, beginning=days_ago_450, end=days_ago_600, twos=12, threes=20,
                                         minutes_played=769, rebounds=12, fouls=34)
jordan_season_4.save()
# Games
######### Soccer
home1 = SoccerGameTeamStatistic(team=barcelona, corner_kicks=12, fouls_offside=2, goal_attempts=8, goals=2,
                                possession=12.12)
home1.save()

away1 = SoccerGameTeamStatistic(team=madrid, corner_kicks=13, fouls_offside=4, goal_attempts=9, goals=3,
                                possession=65.12)
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
########## Basketball
home1 = BasketballGameTeamStatistic(team=magic, twos=120, threes=140, fouls=120, free_throws=980, points=120,
                                    first_quarter_points=90, second_quarter_points=80, third_quarter_points=40,
                                    fourth_quarter_points=24)
home1.save()

away1 = BasketballGameTeamStatistic(team=magic, twos=120, threes=140, fouls=120, free_throws=980, points=120,
                                    first_quarter_points=90, second_quarter_points=80, third_quarter_points=40,
                                    fourth_quarter_points=24)
away1.save()

game1 = BasketballGame(home=home1, away=away1, play_date=timezone.now(), best_player=lebron)
game1.save()

event1 = BasketballEvent(event_time=timezone.now() + timezone.timedelta(minutes=5), game=game1, event_type='AT')
event1.save()

event2 = BasketballEvent(event_time=timezone.now() + timezone.timedelta(minutes=7), game=game1, event_type='2P')
event2.save()

event3 = BasketballEvent(event_time=timezone.now() + timezone.timedelta(minutes=9), game=game1, event_type='3P')
event3.save()

event4 = BasketballEvent(event_time=timezone.now() + timezone.timedelta(minutes=13), game=game1, event_type='PY')
event4.save()

event5 = BasketballEvent(event_time=timezone.now() + timezone.timedelta(minutes=16), game=game1, event_type='PY')
event5.save()

event6 = BasketballEvent(event_time=timezone.now() + timezone.timedelta(minutes=34), game=game1, event_type='SN')
event6.save()
# Leagues
laliga_league = League(name="La Liga", country='Spain', beginning_year=2018, end_year=2019)
laliga_league.save()

fifa_league = League(name="FIFA", country='Hell', beginning_year=2016, end_year=2017)
fifa_league.save()

premiere_league = League(name="Premiere League", beginning_year=2015, end_year=2016)
premiere_league.save()

world_cup_league = League(name="World Cup", country='Heaven', beginning_year=2014, end_year=2015)
world_cup_league.save()

efl_league = League(name="EFL", country='Iraq', beginning_year=2013, end_year=2014)
efl_league.save()

usl_league = League(name="USL", country='Africa', beginning_year=2012, end_year=2013)
usl_league.save()

federation_league = League(name="Federation", beginning_year=2011, end_year=2012)
federation_league.save()
##########
mls_league = League(name="MLS", country='Pakistan', sport='Basketball', beginning_year=2017, end_year=2018)
mls_league.save()

nba_league = League(name="NBA", country='Pakistan', sport='Basketball', beginning_year=2018, end_year=2019)
nba_league.save()

aba_league = League(name="ABA", country='France', sport='Basketball', beginning_year=2016, end_year=2017)
aba_league.save()

greek_league = League(name="Greek", country='Italia', sport='Basketball', beginning_year=2016, end_year=2017)
greek_league.save()
##########
barcelona_in_laliga = SoccerTeamLeagueStatistic(league=laliga_league, team=barcelona, rank=1, games=40, win=25, lose=5,
                                                draw=10, goal_difference=10, score=12)
barcelona_in_laliga.save()

liverpool_in_laliga = SoccerTeamLeagueStatistic(league=laliga_league, team=liverpool, rank=2, games=40, win=25, lose=5,
                                                draw=10, goal_difference=10, score=12)
liverpool_in_laliga.save()

chelsea_in_laliga = SoccerTeamLeagueStatistic(league=laliga_league, team=chelsea, rank=3, games=23, win=12, lose=8,
                                              draw=10, goal_difference=10, score=12)
chelsea_in_laliga.save()
##########
barcelona_in_fifa = SoccerTeamLeagueStatistic(league=fifa_league, team=barcelona, rank=1, games=40, win=25, lose=5,
                                              draw=10, goal_difference=10, score=12)
barcelona_in_fifa.save()

liverpool_in_fifa = SoccerTeamLeagueStatistic(league=fifa_league, team=liverpool, rank=2, games=40, win=25, lose=5,
                                              draw=10, goal_difference=10, score=12)
liverpool_in_fifa.save()

chelsea_in_fifa = SoccerTeamLeagueStatistic(league=fifa_league, team=chelsea, rank=3, games=23, win=12, lose=8,
                                            draw=10, goal_difference=10, score=12)
chelsea_in_fifa.save()
##########
barcelona_in_aba = SoccerTeamLeagueStatistic(league=aba_league, team=barcelona, rank=1, games=40, win=25, lose=5,
                                             draw=10, goal_difference=10, score=12)
barcelona_in_aba.save()

liverpool_in_aba = SoccerTeamLeagueStatistic(league=aba_league, team=liverpool, rank=2, games=40, win=25, lose=5,
                                             draw=10, goal_difference=10, score=12)
liverpool_in_aba.save()

chelsea_in_aba = SoccerTeamLeagueStatistic(league=aba_league, team=chelsea, rank=3, games=23, win=12, lose=8,
                                           draw=10, goal_difference=10, score=12)
chelsea_in_aba.save()
##########
lakers_in_mls = BasketballTeamLeagueStatistic(league=mls_league, team=lakers, rank=1, games=40, win=25, lose=5,
                                              percentage=92.92)
lakers_in_mls.save()

bucks_in_mls = BasketballTeamLeagueStatistic(league=mls_league, team=bucks, rank=2, games=40, win=25, lose=5,
                                             percentage=92.92)
bucks_in_mls.save()

nets_in_mls = BasketballTeamLeagueStatistic(league=mls_league, team=nets, rank=3, games=40, win=25, lose=5,
                                            percentage=92.92)
nets_in_mls.save()

magic_in_mls = BasketballTeamLeagueStatistic(league=mls_league, team=magic, rank=4, games=40, win=25, lose=5,
                                             percentage=92.92)
magic_in_mls.save()
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
