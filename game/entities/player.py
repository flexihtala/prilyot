from pygame import Surface, draw, Rect

from game.entities.base import BaseEntity


class Player(BaseEntity):
    def __init__(self):
        self.sprite_image = Rect(100, 100, 32, 64)

    def render(self, screen: Surface):
        draw.rect(screen, (200, 1, 1), self.sprite_image)

    def move_up(self):
        self.sprite_image.y -= 1

    def move_down(self):
        self.sprite_image.y += 1

    def move_left(self):
        self.sprite_image.x -= 1

    def move_right(self):
        self.sprite_image.x += 1
