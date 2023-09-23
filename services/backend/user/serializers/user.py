from rest_framework import serializers

from user.models import User


class BaseUserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
        )
        read_only_fields = (
            "pk",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
        )
