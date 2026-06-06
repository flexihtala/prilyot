from pygame import Surface, draw, Rect

from game.entities.base import BaseEntity


class Player(BaseEntity):
    def __init__(self):
        self.position = (450, 200)
        self.sprite_image = Rect(450, 200, 32, 64)
        self.speed = 20

    def render(self, screen: Surface):
        draw.rect(screen, (1, 200, 1), self.sprite_image)

    def move_up(self):
        self.sprite_image.y -= self.speed

    def move_down(self):
        self.sprite_image.y += self.speed

    def move_left(self):
        self.sprite_image.x -= self.speed

    def move_right(self):
        self.sprite_image.x += self.speed
