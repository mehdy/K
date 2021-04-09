from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.utils import timezone
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "last_login",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "last_login",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }
        depth = 1

    def validate_password(self, value):
        try:
            password_validation.validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data["last_login"] = timezone.now()
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        if "password" in validated_data:
            instance.set_password(validated_data.pop("password"))
        return super().update(instance, validated_data)
