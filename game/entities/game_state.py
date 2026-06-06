from game.entities.base import BaseEntity
from game.entities.bullet import Bullet
from game.entities.monster import Monster
from game.entities.player import Player
from game.entities.station import Station
from game.entities.timer import Timer


class GameState:
    def __init__(
        self,
        player: Player,
        station: Station,
        timer: Timer,
        bullets: list[Bullet] | None = None,
        monsters: list[Monster] | None = None,
    ):
        self.player = player
        self.station = station
        self.timer = timer
        self.bullets = bullets or []
        self.monsters = monsters or []

    def add_bullet(self, bullet: Bullet):
        self.bullets.append(bullet)

    def add_monster(self, monster: Monster):
        self.monsters.append(monster)

    @property
    def entities(self) -> list[BaseEntity]:
        return [self.player, self.station, self.timer, *self.bullets, *self.monsters]
