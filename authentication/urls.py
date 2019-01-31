from django.conf.urls import url
from django.urls import path

from authentication import views
from authentication.views import CreateUserView, CustomAuthToken

urlpatterns = [
    url('api-token-auth/', CustomAuthToken.as_view()),
    url('sign_up/', CreateUserView.as_view()),
    path('confirm_account/<int:id>/<int:code>/', views.confirm_account),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
