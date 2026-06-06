import random

from game.constants import SCREEN_SIZE
from game.entities.game_state import GameState
from game.entities.monster import Monster
from game.schemas.rectangle import Rectangle as RectangleSchema


class MonsterSpawner:
    def __init__(self):
        self.frame_counter = -1
        self.spawn_period = 0.5

        offset = 25
        left_rect = RectangleSchema(
            x_first=-offset - 50,
            x_second=0,
            y_first=-offset,
            y_second=SCREEN_SIZE[1] + offset,
        )
        up_rect = RectangleSchema(
            x_first=-offset,
            x_second=SCREEN_SIZE[0] + offset,
            y_first=-offset - 50,
            y_second=0,
        )
        right_rect = RectangleSchema(
            x_first=SCREEN_SIZE[0],
            x_second=SCREEN_SIZE[0] + offset,
            y_first=-offset,
            y_second=SCREEN_SIZE[1] + offset,
        )
        down_rect = RectangleSchema(
            x_first=SCREEN_SIZE[0],
            x_second=SCREEN_SIZE[0] + offset,
            y_first=SCREEN_SIZE[1],
            y_second=SCREEN_SIZE[1] + offset,
        )
        self.sectors = [left_rect, up_rect, right_rect, down_rect]

    def spawn_monster(self, game_state: GameState):
        self.frame_counter += 1

        if self.frame_counter % (self.spawn_period * 60) == 0:
            new_monster_position = self._get_new_monster_position()
            new_monster = Monster(position=new_monster_position)
            game_state.add_monster(new_monster)

    def _get_new_monster_position(self) -> list[int]: # [x, y]
        sector = self.sectors[random.randint(0, 3)]
        return [
            random.randint(sector.x_first, sector.x_second),
            random.randint(sector.y_first, sector.y_second),
        ]
