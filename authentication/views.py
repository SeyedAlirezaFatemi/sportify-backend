from rest_auth.registration.views import RegisterView

from authentication.models import User


class CustomRegisterView(RegisterView):
    queryset = User.objects.all()
