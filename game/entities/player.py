from pygame import Surface, Rect, image, transform

from game.entities.base import BaseEntity
from game import constants


class Player(BaseEntity):
    def __init__(self):
        self.position = constants.PLAYER_START_POSITION
        self.width = constants.PLAYER_WIDTH
        self.height = constants.PLAYER_HEIGHT
        self.hitbox = Rect(100, 100, self.width, self.height)
        self.image = transform.scale(
            image.load("assets/player.png").convert_alpha(), (self.width, self.height)
        )
        self.speed = constants.PLAYER_SPEED

    def render(self, screen: Surface):
        screen.blit(self.image, Rect(*self.position, self.width, self.height))

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_right(self):
        self.position[0] += self.speed
