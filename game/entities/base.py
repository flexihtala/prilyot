from __future__ import annotations
from pygame import Surface
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from game.entities.game_state import GameState


class BaseEntity:
    def update(self, game_state: GameState): ...

    def render(self, screen: Surface): ...
