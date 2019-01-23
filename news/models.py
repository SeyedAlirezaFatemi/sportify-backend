from django.conf import settings
from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title


class News(models.Model):
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    brief = models.CharField(max_length=1000, default="")
    text = models.CharField(max_length=50000)
    pub_date = models.DateTimeField()
    image = models.ImageField()
    tags = models.ManyToManyField(to=Tag)
    related_news = models.ManyToManyField(to="self")

    class Meta:
        ordering = ["pub_date"]
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField()
    news = models.ForeignKey(to=News, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ["pub_date"]

    def __str__(self):
        return self.author
