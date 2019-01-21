from django.urls import path

from . import views

urlpatterns = [
    path('statistic/', views.PlayerStatistics.as_view(), name='player_statistic'),
]
