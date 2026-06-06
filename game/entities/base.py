from pygame import Surface


class BaseEntity:
    def update(self): ...

    def render(self, screen: Surface): ...
