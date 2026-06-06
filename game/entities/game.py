from game.entities.base import BaseEntity
from game.entities.game_state import GameState


class Game(BaseEntity):
    def __init__(self, game_state: GameState):


    def update(self):
        ...

    def render(self):
        ...
