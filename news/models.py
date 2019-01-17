from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    title = models.CharField(unique=True)


class News(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField()
    text = models.CharField()
    pub_date = models.DateTimeField()
    image = models.ImageField()
    tags = models.ManyToManyField(to=Tag)
    related_news = models.ManyToManyField(to="self")


class Comment(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.CharField()
    pub_date = models.DateTimeField()
    news = models.ForeignKey(to=News, on_delete=models.CASCADE)
