from rest_framework.serializers import ModelSerializer

from user.models import User
from .models import Event, Option


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ("id", "first_name", "last_name", "username", "email")
        fields = read_only_fields


class OptionSerializer(ModelSerializer):
    voters = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Option
        fields = ("id", "start_at", "finish_at", "voters")
        depth = 1


class EventSerializer(ModelSerializer):
    owner = UserSerializer(read_only=True)
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        read_only_fields = ("id", "owner", "options", "created_at", "updated_at")
        fields = read_only_fields + (
            "title",
            "description",
            "timezone",
            "optional",
            "options",
        )
        depth = 1
