from django.conf.urls import url

from authentication.views import CustomAuthToken

urlpatterns = [
    url(r'^api-token-auth/', CustomAuthToken.as_view())
]
