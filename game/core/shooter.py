from __future__ import annotations
from typing import TYPE_CHECKING

from pygame import Vector2

from game import constants
from game.entities.bullet import Bullet

if TYPE_CHECKING:
    from game.entities.game_state import GameState


class Shooter:
    def __init__(self):
        self.frame_counter = -1
        self.shooting_period = 0.25
        self.offset = Vector2(constants.PLAYER_WIDTH / 2, constants.PLAYER_HEIGHT / 2)

    def shoot(self, game_state: GameState, player_pos: list[int], mouse_pos: list[int]):
        self.frame_counter += 1

        if self.frame_counter % (self.shooting_period * 60) == 0:
            bullet = Bullet(player_pos + self.offset, mouse_pos)
            game_state.add_bullet(bullet)
