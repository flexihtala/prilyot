from game import constants
from game.entities.base import BaseEntity


class Task(BaseEntity):
    def __init__(self):
        self.tasks_number = 0
        self.task_position = constants.TASK_POSITION


    # def show_task(self, screen: Surface):
    #     current_task = self.tasks[self.tasks_number % len(self.tasks)]
    #     screen.blit(current_task.image, Rect(*self.task_position, self.width, self.height))
    #     self.tasks_number += 1