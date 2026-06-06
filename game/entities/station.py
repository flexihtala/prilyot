from pygame import Rect, image, transform, Surface

from game.entities.base import BaseEntity
from game import constants
from game.schemas.task import Task


class Station(BaseEntity):
    def __init__(self):
        self.position = constants.STATION_POSITION
        self.width = constants.STATION_WIDTH
        self.height = constants.STATION_HEIGHT
        self.image = transform.scale(
            image.load("assets/station.png").convert_alpha(), (self.width, self.height)
        )
        self.hitbox = Rect(*self.position, self.width, self.height)

        self.tasks = [
            Task(
                image=transform.scale(
                    image.load("assets/tasks/task_1.png").convert_alpha(), (100, 100)
                ),
                correct_answer="12",
            ),
        ]

    def render(self, screen: Surface):
        screen.blit(self.image, Rect(*self.position, self.width, self.height))
