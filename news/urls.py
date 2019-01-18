from django.urls import path

from . import views

urlpatterns = [
    path('', views.LatestNews.as_view(), name='latest_news')
]
