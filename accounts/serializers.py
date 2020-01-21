import jwt

from datetime import timedelta
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer with only basic information.
    """

    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'password'
        ]

    def create(self, validated_data):
        user = self.Meta.model.objects.create_user(**validated_data)
        return user
