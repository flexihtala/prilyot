from __future__ import annotations
from typing import TYPE_CHECKING

from pygame import Surface, Rect, draw, Vector2

from game.entities.base import BaseEntity

if TYPE_CHECKING:
    from game.entities.game_state import GameState


class Bullet(BaseEntity):
    def __init__(self, position: Vector2, direction: list[int]):
        self.position = position
        self.init_position = position
        self.direction = Vector2(direction)
        self.width = 10
        self.hitbox = Rect(*self.position, self.width, self.width)
        self.speed_coef = 20
        self.frame_counter = -1
        self.time_to_live = 1
        self.should_be_deleted = False

    def update(self, game_state: GameState):
        self.frame_counter += 1

        if abs(self.frame_counter - self.time_to_live * 60) < 0.0001:
            self.should_be_deleted = True

        dir_vector = self.direction - Vector2(self.init_position)
        norm_dir_vector = dir_vector.normalize()
        new_position = [
            self.position[0] + norm_dir_vector[0] * self.speed_coef,
            self.position[1] + norm_dir_vector[1] * self.speed_coef,
        ]
        self.position = new_position
        self.hitbox = Rect(self.position[0], self.position[1], self.width, self.width)

        self._check_collisions(game_state)

    def render(self, screen: Surface):
        draw.circle(
            screen, color="white", center=self.hitbox.center, radius=self.width / 2
        )
        draw.circle(
            screen, color="black", center=self.hitbox.center, radius=self.width / 2 - 1
        )

    def _check_collisions(self, game_state: GameState):
        for monster in game_state.monsters:
            if monster.hitbox.colliderect(self.hitbox):
                self.should_be_deleted = True
                monster.on_death(game_state)
