from __future__ import annotations
from typing import TYPE_CHECKING

from pygame import transform, image, Surface, Rect, font, draw

from game import constants
from game.entities.base import BaseEntity
from game.entities.enums import TaskStatus

if TYPE_CHECKING:
    from game.entities.game_state import GameState

from game.schemas.task import TaskSchema


class Task(BaseEntity):
    def __init__(self) -> None:
        self.tasks_number = 0
        self.task_position = constants.TASK_POSITION
        self.width = constants.TASK_WIDTH
        self.height = constants.TASK_HEIGHT
        self.tasks = [
            TaskSchema(
                image=transform.scale(
                    image.load("assets/tasks/task_1.png").convert_alpha(),
                    (self.width, self.height),
                ),
                correct_answer="12",
            ),
        ]
        self.status = TaskStatus.close
        self.current_text = ""
        self.font = font.Font(None, 48)

    def update(self, game_state: GameState):
        if self.status is not TaskStatus.enter:
            return

        current_task = self.tasks[self.tasks_number % len(self.tasks)]
        if self.current_text != current_task.correct_answer:
            self.status = TaskStatus.close
            self.current_text = ""
            print("Плохо ответ")
            return

        game_state.timer.add_time(constants.TASK_TIME_PLUS)
        print("Хороший ответ")
        self.status = TaskStatus.close
        self.current_text = ""

    def render(self, screen: Surface):
        if self.status not in TaskStatus.open:
            return

        current_task = self.tasks[self.tasks_number % len(self.tasks)]
        screen.blit(
            current_task.image, Rect(*self.task_position, self.width, self.height)
        )

        draw.rect(
            screen,
            constants.GREY,
            Rect(
                *constants.TASK_TEXT_POSITION,
                constants.TASK_WIDTH,
                constants.TASK_TEXT_WIDTH,
            ),
        )
        text_surface = self.font.render(self.current_text, True, constants.WHITE)
        screen.blit(text_surface, (430, 830))
