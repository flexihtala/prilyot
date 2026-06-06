import random

from pygame import Surface, Rect, transform, image
from pygame.math import Vector2

from game.entities.base import BaseEntity


class Monster(BaseEntity):
    def __init__(self, position) -> None:
        self.position = position
        self.width = 64
        self.height = 128
        self.sprite_image = Rect(
            self.position[0], self.position[1], self.width, self.height
        )
        image_name = self._get_image()
        self.image = transform.scale(image.load(image_name).convert_alpha(), (64, 128))
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
        screen.blit(self.image, self.sprite_image)

    def _get_image(self):
        number = random.randint(1, 5)
        return f"assets/monster_{number}.png"
