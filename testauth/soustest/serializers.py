from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
#extra_kwargs = {'password': {'write_only': True, 'required': True}}

def create(self,validated_data):
        user = User.objects.create_user(**validated_data)

        return user

class SignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User

        def create(self,validated_data):
            user = User.objects.create_superuser(self,
                                        )