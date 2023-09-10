from core.views.base import BaseVueView
from random import randint

class ExampleView(BaseVueView):
    component_name = "hello"

    def get_component_props(self) -> dict:
        return {"msg": "Hello World!"}
