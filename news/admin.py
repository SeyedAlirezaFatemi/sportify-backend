from django.contrib import admin

from .models import Comment, News, Tag

admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Tag)
