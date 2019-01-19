from django.utils import timezone

from authentication.models import User
from news.models import News, Tag

tag1 = Tag(title='Iran')
tag1.save()
tag2 = Tag(title='Spain')
tag2.save()
tag3 = Tag(title='National')
tag3.save()
tag4 = Tag(title='Global')
tag4.save()
tag5 = Tag(title='2019')
tag5.save()
tag6 = Tag(title='2018')
tag6.save()
tag7 = Tag(title='Rain')
tag7.save()

test_user = User.objects.get(pk=1)

news1 = News(author=test_user, title='Big Explosion',
             text="""The official told CNN that Trump's idea is to put something on the table to get Democrats to engage with negotiations.
             Trump is not expected to back down from his demand for a border wall, but the plan will seek to entice Democrats by offering other concessions.
             """
             , pub_date=timezone.now())
news1.save()
news1.tags.add(tag1, tag2, tag3)
