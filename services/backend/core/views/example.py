from core.views.base import BaseVueView

class ExampleView(BaseVueView):
    component_name = "hello"

    def get_component_props(self) -> dict:
        return {"msg": "Hello World!"}
