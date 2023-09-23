from rest_framework import serializers

from core.views.base import BaseVueView
from user.models import User
from user.serializers.user import BaseUserGetSerializer


class ExampleViewSerializer(serializers.Serializer):
    msg = serializers.CharField()


class ExampleView(BaseVueView):
    component_name = "hello"
    serializer = ExampleViewSerializer

    def get_component_props(self) -> dict:
        return dict(
            msg="Hello World!",
        )


class ExampleUsersSerializer(serializers.Serializer):
    users = BaseUserGetSerializer(many=True)


class UserListExampleView(BaseVueView):
    component_name = "users"
    serializer = ExampleUsersSerializer

    def get_component_props(self) -> dict:
        return dict(
            users=User.objects.all(),
        )
