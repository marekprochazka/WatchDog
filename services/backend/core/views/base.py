import abc
import json
from typing import Type, TypeVar

from django.views.generic import TemplateView
from rest_framework import serializers

from user.models import User
from user.serializers.user import BaseUserGetSerializer

S = TypeVar("S", bound=serializers.Serializer)


class BaseVueView(TemplateView, abc.ABC):
    template_name = "base.html"

    component_name: str = None
    component_props: dict = {}
    serializer: Type[S] = None

    def get_serialized_user_data(self) -> User | dict:
        return (
            dict(BaseUserGetSerializer(self.request.user).data)
            if self.request.user.is_authenticated
            else None
        )

    def get_serializer_class(self) -> Type[S] | None:
        return self.serializer

    def get_component_props(self) -> dict:
        return self.component_props

    def get_serializer(self) -> S | None:
        if (s := self.get_serializer_class()) is not None:
            return s({**self.get_component_props()})
        return None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.component_name is None:
            raise ValueError("component_name must be defined")

    def validated_props(self) -> dict:
        serializer = self.get_serializer()
        if serializer is None:
            raise ValueError(
                "serializer or get_serializer must be defined must be defined"
            )
        if not issubclass(type(serializer), serializers.Serializer):
            raise ValueError(
                "serializer must be subclass of rest_framework.serializers.Serializer"
            )
        return serializer.data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["component_name"] = self.component_name
        props = self.validated_props()
        context["component_props"] = json.dumps(props)
        return context
