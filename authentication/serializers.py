from rest_auth.registration.serializers import RegisterSerializer, serializers
from authentication.models import User


class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
            'name': self.validated_data.get('name', ''),
        }


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name')
        read_only_fields = ('email',)
