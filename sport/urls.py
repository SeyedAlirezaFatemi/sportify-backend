from django.urls import path

from . import views

urlpatterns = [
    path('player/info/<int:pk>/', views, name='latest_news'),
]
