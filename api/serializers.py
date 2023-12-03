from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers, validators
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'password', 'role']

        extra_kwargs = {
            'username': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        get_user_model().objects.all(), 'Username already in use'
                    )
                ]
            },
            'password': {
                'write_only': True,
                'required': True,
                'allow_blank': False
            },
            'role': {
                'required': True,
                'allow_blank': False
            },
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        role = validated_data.get('role')

        user = get_user_model().objects.create(
            username=username,
            password=make_password(password),
            role=role,
        )

        return user
