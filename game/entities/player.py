from pygame import Surface, draw, Rect

from game.entities.base import BaseEntity


class Player(BaseEntity):
    def __init__(self):
        self.sprite_image = Rect(100, 100, 64, 128)
        self.speed = 20

    def render(self, screen: Surface):
        draw.rect(screen, (200, 1, 1), self.sprite_image)

    def move_up(self):
        self.sprite_image.y -= self.speed

    def move_down(self):
        self.sprite_image.y += self.speed

    def move_left(self):
        self.sprite_image.x -= self.speed

    def move_right(self):
        self.sprite_image.x += self.speed
