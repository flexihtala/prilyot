from pygame import Surface


class BaseEntity:
    def update(self, game_state): ...

    def render(self, screen: Surface): ...
