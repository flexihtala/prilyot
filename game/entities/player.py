from pygame import Surface, draw, Rect

from game.entities.base import BaseEntity


class Player(BaseEntity):
    def __init__(self):
        self.position = [450, 200]
        self.width = 32
        self.height = 64
        self.sprite_image = Rect(450, 200, 32, 64)
        self.speed = 5

    def render(self, screen: Surface):
        draw.rect(screen, (1, 200, 1), Rect(*self.position, self.width, self.height))

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_right(self):
        self.position[0] += self.speed
