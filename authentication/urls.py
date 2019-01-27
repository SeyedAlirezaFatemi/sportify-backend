from django.conf.urls import url

from authentication.views import CreateUserView, CustomAuthToken

urlpatterns = [
    url('api-token-auth/', CustomAuthToken.as_view()),
    url('sign_up/', CreateUserView.as_view()),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
