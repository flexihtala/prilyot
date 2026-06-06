from pygame import Surface, transform, image
from game import constants

from game.entities.base import BaseEntity
from game.entities.game_state import GameState


class Game(BaseEntity):
    def __init__(self, game_state: GameState):
        self.game_state = game_state
        self.map = transform.scale(image.load("assets/map.png").convert_alpha(), constants.SCREEN_SIZE)

    def update(self):
        for entity in self.game_state.entities:
            entity.update(self.game_state)

    def render(self, screen: Surface):
        screen.blit(self.map, (0,0 ))
        for entity in self.game_state.entities:
            entity.render(screen)
