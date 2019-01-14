from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    title = models.CharField(unique=True)


class News(models.Model):
    author = models.ForeignKey(to=User)
    title = models.CharField()
    text = models.CharField()
    pub_date = models.DateTimeField()
    image = models.ImageField()
    tags = models.ManyToManyField(to=Tag)


class Comment(models.Model):
    author = models.ForeignKey(to=User)
    text = models.CharField()
    pub_date = models.DateTimeField()
    news = models.ForeignKey(to=News)
