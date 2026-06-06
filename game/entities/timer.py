from __future__ import annotations
from datetime import datetime, UTC
from typing import TYPE_CHECKING
import pygame
from game.entities.base import BaseEntity

from pygame import Surface, Rect
from game import constants

if TYPE_CHECKING:
    from game.entities.game_state import GameState


class Timer(BaseEntity):
    def __init__(self):
        self.position = constants.TIMER_POSITION
        self.width = constants.TIMER_WIDTH
        self.height = constants.TIMER_HEIGHT
        self.time = constants.TIMER_TIME_IN_SECONDS
        self.border_line_coef = constants.TIMER_BORDER_LINE_COEF

        self.remaining_time = self.time
        self.current_real_time = datetime.now(UTC)

        self.border_rect = (
            Rect(
                self.position[0] - self.border_line_coef,
                self.position[1] - self.border_line_coef,
                self.width + 2 * self.border_line_coef,
                self.height + 2 * self.border_line_coef,
            ),
        )

        self.inside_fixed_rect = (
            Rect(
                self.position[0],
                self.position[1],
                self.width,
                self.height,
            ),
        )

        self.inside_timer_rect = self.inside_fixed_rect

    def render(self, screen: Surface):
        pygame.draw.rect(screen, (0, 0, 0), self.border_rect)

        pygame.draw.rect(screen, (255, 255, 255), self.inside_fixed_rect)

        pygame.draw.rect(screen, (0, 0, 128), self.inside_timer_rect)

    def update(self, game_state: GameState):
        self.remaining_time -= (
            datetime.now(UTC) - self.current_real_time
        ).total_seconds()
        if self.remaining_time <= 0:
            raise RuntimeError("Время вышло")

        current_width = (self.remaining_time / self.time) * self.width

        self.inside_timer_rect = Rect(
            self.position[0], self.position[1], current_width, self.height
        )
        self.current_real_time = datetime.now(UTC)

    def add_time(self, seconds: int):
        self.remaining_time = min(self.remaining_time + seconds, self.time)
