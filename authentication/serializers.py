from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string
from rest_auth.registration.serializers import RegisterSerializer, serializers

from authentication.models import User


class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
        }

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        generated_conf_code = get_random_string(length=6)
        user.confirmation_code = generated_conf_code
        user.save()
        email_message = EmailMessage('Confirm your account!',
                                     'hiring/confirm_employer/' + str(user.id) + '/' + str(generated_conf_code), '',
                                     [validated_data['email']])
        email_message.send()
        return user

    class Meta:
        model = User
        fields = ("id", "email", "password",)


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)
        read_only_fields = ('email',)
