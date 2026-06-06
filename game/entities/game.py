from pygame import Surface

from game.entities.base import BaseEntity
from game.entities.game_state import GameState


class Game(BaseEntity):
    def __init__(self, game_state: GameState):
        self.game_state = game_state

    def update(self):
        for entity in self.game_state.entities:
            entity.update(self.game_state)

    def render(self, screen: Surface):
        for entity in self.game_state.entities:
            entity.render(screen)
