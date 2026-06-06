from pygame import Rect, image, transform, Surface

from game.entities.base import BaseEntity
from game import constants


class Station(BaseEntity):
    def __init__(self):
        self.position = constants.STATION_POSITION
        self.width = constants.STATION_WIDTH
        self.height = constants.STATION_HEIGHT
        self.image = transform.scale(
            image.load("assets/station.png").convert_alpha(), (self.width, self.height)
        )
        self.hitbox = Rect(*self.position, self.width, self.height)

    def render(self, screen: Surface):
        screen.blit(self.image, Rect(*self.position, self.width, self.height))
