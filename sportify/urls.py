from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('verified-email-field/', include('verified_email_field.urls')),
    path('news/', include('news.urls')),
    path('sport/', include('sport.urls')),
]
