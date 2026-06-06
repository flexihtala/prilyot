from pygame import Surface, Rect, image, transform

from game.entities.base import BaseEntity


class Player(BaseEntity):
    def __init__(self):
        self.position = [100, 100]
        self.width = 64
        self.height = 128
        self.hitbox = Rect(100, 100, 64, 128)
        self.image = transform.scale(
            image.load("assets/player.png").convert_alpha(), (64, 128)
        )
        self.speed = 5

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
