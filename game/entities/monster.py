import random
from datetime import datetime, UTC, timedelta

import pygame
from pygame import Surface, Rect, transform, image
from pygame.math import Vector2

from game.entities.base import BaseEntity


class Monster(BaseEntity):
    def __init__(self, position: list[int]) -> None:
        self.index = random.randint(1, 5)
        self.position = position
        self.width = 96
        self.height = 192
        self.hitbox = Rect(*self.position, self.width, self.height)
        self.image = transform.scale(image.load(f"assets/monster_{self.index}.png").convert_alpha(), (96, 192))
        self.sound = pygame.mixer.Sound(f"assets/sounds/death_sound_{self.index}.wav")

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

    def on_death(self, game_state):
        self.sound.play()
        game_state.monsters.remove(self)
