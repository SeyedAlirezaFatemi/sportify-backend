from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.crypto import get_random_string
from rest_auth.registration.views import RegisterView
from rest_framework import permissions, status, serializers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import generics

from authentication.models import User
from authentication.serializers import UserSerializer


class CustomRegisterView(RegisterView):
    queryset = User.objects.all()


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'userId': user.pk,
            'email': user.email
        })


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer


# @api_view(['POST'])
# def create_auth(request):
#     serialized = UserSerializer(data=request.DATA)
#     if serialized.is_valid():
#         User.objects.create_user(
#             serialized.init_data['email'],
#             # serialized.init_data['username'],
#             serialized.init_data['password']
#         )
#         return Response(serialized.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)



@api_view()
def confirm_account(request, id, code):
    user = User.objects.get(id=id)
    activate = False
    if user.confirmation_code == code:
        user.is_active = True
        user.save()
        activate = True
    response = {'activate': activate}
    return Response(response)
