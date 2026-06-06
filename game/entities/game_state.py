from game.entities.base import BaseEntity
from game.entities.bullet import Bullet
from game.entities.monster import Monster
from game.entities.player import Player
from game.entities.station import Station
from game.entities.task import Task
from game.entities.timer import Timer


class GameState:
    def __init__(
        self,
        player: Player,
        station: Station,
        timer: Timer,
        task: Task,
        bullets: list[Bullet] | None = None,
        monsters: list[Monster] | None = None,
    ):
        self.player = player
        self.station = station
        self.timer = timer
        self.task = task
        self.bullets = bullets or []
        self.monsters = monsters or []

    def add_bullet(self, bullet: Bullet):
        self.bullets.append(bullet)

    def add_monster(self, monster: Monster):
        self.monsters.append(monster)

    @property
    def entities_for_update(self) -> list[BaseEntity]:
        return [
            self.player,
            self.station,
            self.timer,
            self.task,
            *self.bullets,
            *self.monsters,
        ]

    @property
    def entities_for_render(self) -> list[BaseEntity]:
        return [
            self.station,
            self.player,
            *self.bullets,
            *self.monsters,
            self.timer,
            self.task,
        ]
