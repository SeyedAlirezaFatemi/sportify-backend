from django.utils import timezone

from authentication.models import User
from news.models import Comment, News, Tag
from sport.models import BasketballEvent, BasketballGame, BasketballGameTeamStatistic, BasketballPlayer, \
    BasketballPlayerImage, BasketballPlayerSeason, BasketballTeam, BasketballTeamLeagueStatistic, League, PersonAvatar, \
    PlayerVideo, SoccerEvent, SoccerGame, SoccerGameTeamStatistic, SoccerGameVideo, SoccerPlayer, SoccerPlayerSeason, \
    SoccerTeam, SoccerTeamImage, SoccerTeamLeagueStatistic, SoccerTeamVideo, TeamLogo, BasketballGameVideo, \
    BasketballTeamVideo

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
barcelona_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/paYnEE8hcrP96neHRNofhQ_96x96.png')
barcelona_logo.save()
barcelona = SoccerTeam(name='Barcelona', logo=barcelona_logo)
barcelona.save()
barcelona_image_1 = SoccerTeamImage(team=barcelona,
                                    address="https://secure.i.telegraph.co.uk/multimedia/archive/03459/iranian-womens-foo_3459298b.jpg")
barcelona_image_1.save()
barcelona_video_1 = SoccerTeamVideo(youtube_id='2g811Eo7K8U', soccer_team=barcelona)
barcelona_video_1.save()
barcelona_video_2 = SoccerTeamVideo(youtube_id='p28xueW134o', soccer_team=barcelona)
barcelona_video_2.save()
barcelona_video_3 = SoccerTeamVideo(youtube_id='c5B8HRA09aw', soccer_team=barcelona)
barcelona_video_3.save()

chelsea_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/fhBITrIlbQxhVB6IjxUO6Q_96x96.png')
chelsea_logo.save()
chelsea = SoccerTeam(name='Chelsea', logo=chelsea_logo)
chelsea.save()
chelsea_video_1 = SoccerTeamVideo(youtube_id='U32_-UE3VHM', soccer_team=chelsea)
chelsea_video_1.save()
chelsea_video_2 = SoccerTeamVideo(youtube_id='p-S91FoV4bs', soccer_team=chelsea)
chelsea_video_2.save()
chelsea_video_3 = SoccerTeamVideo(youtube_id='hWGdRrfgB2s', soccer_team=chelsea)
chelsea_video_3.save()

liverpool_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/0iShHhASp5q1SL4JhtwJiw_96x96.png')
liverpool_logo.save()
liverpool = SoccerTeam(name='Liverpool', logo=liverpool_logo)
liverpool.save()
liverpool_video_1 = SoccerTeamVideo(youtube_id='qAhKgMcMhIA', soccer_team=liverpool)
liverpool_video_1.save()
liverpool_video_2 = SoccerTeamVideo(youtube_id='ytCrcO_dm7U', soccer_team=liverpool)
liverpool_video_2.save()
liverpool_video_3 = SoccerTeamVideo(youtube_id='McuTOy4IBFo', soccer_team=liverpool)
liverpool_video_3.save()

madrid_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/Th4fAVAZeCJWRcKoLW7koA_96x96.png')
madrid_logo.save()
madrid = SoccerTeam(name='Madrid', logo=madrid_logo)
madrid.save()
madrid_video_1 = SoccerTeamVideo(youtube_id='awk5LH-SHAo', soccer_team=madrid)
madrid_video_1.save()
madrid_video_2 = SoccerTeamVideo(youtube_id='Ktyjqu470wo', soccer_team=madrid)
madrid_video_2.save()

munich_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/-_cmntP5q_pHL7g5LfkRiw_96x96.png')
munich_logo.save()
munich = SoccerTeam(name='Munich', logo=munich_logo)
munich.save()
munich_video_1 = SoccerTeamVideo(youtube_id='awk5LH-SHAo', soccer_team=munich)
munich_video_1.save()
munich_video_2 = SoccerTeamVideo(youtube_id='Ktyjqu470wo', soccer_team=munich)
munich_video_2.save()

juventus_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/Lv6xmBlUIpN3GAFhtf6nqQ_96x96.png')
juventus_logo.save()
juventus = SoccerTeam(name='Juventus', logo=juventus_logo)
juventus.save()
juventus_video_1 = SoccerTeamVideo(youtube_id='Ktyjqu470wo', soccer_team=juventus)
juventus_video_1.save()
# Basketball Teams
lakers_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/4ndR-n-gall7_h3f7NYcpQ_96x96.png')
lakers_logo.save()
lakers = BasketballTeam(name='Lakers', logo=lakers_logo)
lakers.save()
lakers_video_1 = BasketballTeamVideo(youtube_id='AuJNn43Ws6I', basketball_team=lakers)
lakers_video_1.save()
lakers_video_2 = BasketballTeamVideo(youtube_id='HgYDvi_8Cas', basketball_team=lakers)
lakers_video_2.save()

celtics_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/GDJBo7eEF8EO5-kDHVpdqw_96x96.png')
celtics_logo.save()
celtics = BasketballTeam(name='Celtics', logo=celtics_logo)
celtics.save()
celtics_video_1 = BasketballTeamVideo(youtube_id='ooyqP_RHmPQ', basketball_team=celtics)
celtics_video_1.save()

bucks_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/Wd6xIEIXpfqg9EZC6PAepQ_96x96.png')
bucks_logo.save()
bucks = BasketballTeam(name='Bucks', logo=bucks_logo)
bucks.save()
bucks_video_1 = BasketballTeamVideo(youtube_id='HrWg9quUSeA', basketball_team=celtics)
bucks_video_1.save()

wizards_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/NBkMJapxft4V5kvufec4Jg_96x96.png')
wizards_logo.save()
wizards = BasketballTeam(name='Wizards', logo=wizards_logo)
wizards.save()
wizards_video_1 = BasketballTeamVideo(youtube_id='DEYRPOQfRU4', basketball_team=celtics)
wizards_video_1.save()

hornets_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/ToeKy5-TrHAnTCl-qhuuHQ_96x96.png')
hornets_logo.save()
hornets = BasketballTeam(name='Hornets', logo=hornets_logo)
hornets.save()

jazz_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/SP_dsmXEKFVZH5N1DQpZ4A_96x96.png')
jazz_logo.save()
jazz = BasketballTeam(name='Jazz', logo=jazz_logo)
jazz.save()

bulls_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/ofjScRGiytT__Flak2j4dg_96x96.png')
bulls_logo.save()
bulls = BasketballTeam(name='Bulls', logo=bulls_logo)
bulls.save()

nets_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/iishUmO7vbJBE7iK2CZCdw_96x96.png')
nets_logo.save()
nets = BasketballTeam(name='Nets', logo=nets_logo)
nets.save()

suns_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/pRr87i24KHWH0UuAc5EamQ_96x96.png')
suns_logo.save()
suns = BasketballTeam(name='Suns', logo=suns_logo)
suns.save()

magic_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/p69oiJ4LDsvCJUDQ3wR9PQ_96x96.png')
magic_logo.save()
magic = BasketballTeam(name='Magic', logo=magic_logo)
magic.save()

pacers_logo = TeamLogo(address='https://ssl.gstatic.com/onebox/media/sports/logos/andumiE_wrpDpXvUgqCGYQ_96x96.png')
pacers_logo.save()
pacers = BasketballTeam(name='Pacers', logo=pacers_logo)
pacers.save()
# Soccer Players
ahmad_avatar = PersonAvatar(address='http://www.gstatic.com/tv/thumb/persons/501949/501949_v9_ba.jpg')
ahmad_avatar.save()
ahmad = SoccerPlayer(team=barcelona, name='Ahmad', age=24, nationality='Iran', position='Defender', avatar=ahmad_avatar)
ahmad.save()
ahmad_video_1 = PlayerVideo(youtube_id='bKDdT_nyP54', player=ahmad)
ahmad_video_1.save()
ahmad_video_2 = PlayerVideo(youtube_id='kRlSFm519Bo', player=ahmad)
ahmad_video_2.save()

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

reza_avatar = PersonAvatar(
    address='http://photo.elcinema.com.s3.amazonaws.com/uploads/_640x_b0b4e6287fb03c275d49a89dfa3f3d751890d25005335be416d627c838e94efe.jpg')
reza_avatar.save()
reza = SoccerPlayer(team=barcelona, name='Reza', age=24, nationality='Iran', position='Defender', avatar=reza_avatar)
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
lebron_avatar = PersonAvatar(
    address='http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/1966.png&w=350&h=254')
lebron_avatar.save()
lebron = BasketballPlayer(team=lakers, name='Lebron James', age=33, nationality='American', position='Shooting Guard',
                          avatar=lebron_avatar)
lebron.save()
lebron_image_1 = BasketballPlayerImage(player=lebron,
                                       address='http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/1966.png&w=350&h=254')
lebron_image_1.save()

lebron_image_2 = BasketballPlayerImage(player=lebron,
                                       address='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUL1G7E51wtejCgJeO8q9skosuwB-84p9ACoYJzfWfr9LqGmSH')
lebron_image_2.save()
lebron_video_1 = PlayerVideo(youtube_id='HyznrdDSSGM', player=lebron)
lebron_video_1.save()
lebron_video_2 = PlayerVideo(youtube_id='AqNDk_UJW4k', player=lebron)
lebron_video_2.save()

jordan_avatar = PersonAvatar(
    address='https://images.solecollector.com/complex/image/upload/rzwnlls4oj5bexk0aekf.jpg')
jordan_avatar.save()
jordan = BasketballPlayer(team=jazz, name='Michael Jordan', age=33, nationality='American', position='Shooting Guard',
                          avatar=jordan_avatar)
jordan.save()

harden_avatar = PersonAvatar(
    address='https://imagesvc.timeincapp.com/v3/fan/image?url=https%3A%2F%2Fhouseofhouston.com%2Ffiles%2F2015%2F03%2Fjames-harden-nba-houston-rockets-denver-nuggets2.jpg&c=sc&w=850&h=560')
harden_avatar.save()
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

soccer_game_video_1 = SoccerGameVideo(youtube_id='WNeLUngb-Xg', game=game1)
soccer_game_video_1.save()
soccer_game_video_2 = SoccerGameVideo(youtube_id='78MGzBNHn8k', game=game1)
soccer_game_video_2.save()
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

basketball_game_video_1 = BasketballGameVideo(youtube_id='tIj2ms-lYTI', game=game1)
basketball_game_video_1.save()
basketball_game_video_2 = BasketballGameVideo(youtube_id='ZWDkVqEk2mg', game=game1)
basketball_game_video_2.save()
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
             , pub_date=timezone.now(),
             brief="Nobody knows!",
             image_address='https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Youth-soccer-indiana.jpg/1920px-Youth-soccer-indiana.jpg')
news1.save()
news1.tags.add(iran_tag, spain_tag, national_tag)
news1_comment = Comment(author=test_user, text="Nice!", pub_date=timezone.now(), news=news1)
news1_comment.save()

news2 = News(author=test_user, title="Jones 'fit and ready' to face Rangers",
             text="""Kilmarnock manager Steve Clarke insists he will have no hesitation in playing Jordan Jones against Rangers on Wednesday.
             The 24-year-old winger signed a pre-contract agreement with Killie's title rivals last week and will join Rangers on a four-year contract in the summer.
             """
             , pub_date=timezone.now(),
             brief="Kilmarnock manager Steve Clarke insists he will have no hesitation in playing Jordan Jones against Rangers on Wednesday.",
             image_address='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwABkJsTIpRNDyJCIVjEAhL20W7mhC6mg738GUsfTSIzmPoexx')
news2.save()
news2.tags.add(national_tag, global_tag, tag_2019)
