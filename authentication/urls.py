from django.conf.urls import include, url
from django.urls import path

from authentication.views import CustomAuthToken

urlpatterns = [
    url('api-token-auth/', CustomAuthToken.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
