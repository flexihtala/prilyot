import random
from datetime import datetime, UTC, timedelta
from pygame import Surface, Rect, transform, image
from pygame.math import Vector2

from game.entities.base import BaseEntity


class Monster(BaseEntity):
    def __init__(self, position: list[int]) -> None:
        self.position = position
        self.width = 96
        self.height = 192
        self.hitbox = Rect(*self.position, self.width, self.height)
        image_name = self._get_image()
        self.image = transform.scale(image.load(image_name).convert_alpha(), (96, 192))
        self.speed_coef = 2

        self.damage = 10
        self.last_damage_at: datetime | None = None

    def update(self, game_state):
        player = game_state.player

        player_pos = player.position
        movement_vector = Vector2(
            player_pos[0] - self.position[0], player_pos[1] - self.position[1]
        )
        norm_mov_vector = movement_vector.normalize()
        new_position = [
            self.position[0] + norm_mov_vector[0] * self.speed_coef,
            self.position[1] + norm_mov_vector[1] * self.speed_coef,
        ]
        self.position = new_position
        self.hitbox = Rect(self.position[0], self.position[1], self.width, self.height)

        if player.hitbox.colliderect(self.hitbox):
            if not self.last_damage_at or (
                (datetime.now(UTC) - self.last_damage_at) > timedelta(seconds=1)
            ):
                player.set_damage(self.damage)
                self.last_damage_at = datetime.now(UTC)

    def render(self, screen: Surface):
        screen.blit(self.image, self.hitbox)

    def _get_image(self):
        number = random.randint(1, 5)
        return f"assets/monster_{number}.png"
