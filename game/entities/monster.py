from pygame import Surface, draw, Rect
from pygame.math import Vector2

from game.entities.base import BaseEntity


class Monster(BaseEntity):
    def __init__(self, position) -> None:
        self.position = position
        self.width = 32
        self.height = 64
        self.sprite_image = Rect(
            self.position[0], self.position[1], self.width, self.height
        )
        self.speed_coef = 2

    def update(self, game_state):
        player_pos = game_state.player.position
        movement_vector = Vector2(
            player_pos[0] - self.position[0], player_pos[1] - self.position[1]
        )
        norm_mov_vector = movement_vector.normalize()
        new_position = [
            self.position[0] + norm_mov_vector[0] * self.speed_coef,
            self.position[1] + norm_mov_vector[1] * self.speed_coef,
        ]
        self.position = new_position
        self.sprite_image = Rect(
            self.position[0], self.position[1], self.width, self.height
        )

    def render(self, screen: Surface):
        draw.rect(screen, (200, 1, 1), self.sprite_image)
