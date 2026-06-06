from pygame import Surface, draw, Rect, image, transform

from game.entities.base import BaseEntity


class Player(BaseEntity):
    def __init__(self):
        self.hitbox = Rect(100, 100, 64, 128)
        self.image = transform.scale(image.load("assets/player.png").convert_alpha(), (64, 128))
        self.speed = 10

    def render(self, screen: Surface):
        screen.blit(self.image, self.hitbox)

    def move_up(self):
        self.hitbox.y -= self.speed

    def move_down(self):
        self.hitbox.y += self.speed

    def move_left(self):
        self.hitbox.x -= self.speed

    def move_right(self):
        self.hitbox.x += self.speed
