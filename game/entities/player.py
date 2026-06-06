from __future__ import annotations
from pygame import Surface, Rect, image, transform

from game.core.shooter import Shooter
from game.entities.base import BaseEntity
from game import constants
from typing import TYPE_CHECKING

from game.entities.station import Station

if TYPE_CHECKING:
    from game.entities.game_state import GameState


class Player(BaseEntity):
    def __init__(self):
        self.position = constants.PLAYER_START_POSITION
        self.width = constants.PLAYER_WIDTH
        self.height = constants.PLAYER_HEIGHT
        self.hitbox = Rect(*self.position, self.width, self.height)
        self.image = transform.scale(
            image.load("assets/player.png").convert_alpha(), (self.width, self.height)
        )
        self.speed = constants.PLAYER_SPEED
        self.is_freeze = False
        self.health = 100

        self.shooter = Shooter()

    def is_near_station(self, station: Station) -> bool:
        return self.hitbox.colliderect(station.hitbox)

    def update(self, game_state: GameState):
        self.hitbox = Rect(*self.position, self.width, self.height)

    def render(self, screen: Surface):
        screen.blit(self.image, self.hitbox)

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_right(self):
        self.position[0] += self.speed

    def set_damage(self, damage: int = 5) -> None:
        self.health -= damage
        if self.health <= 0:
            raise RuntimeError("Ты умер")

    def shoot(self, game_state: GameState, mouse_pos: list[int]) -> None:
        self.shooter.shoot(game_state, self.position, mouse_pos)
