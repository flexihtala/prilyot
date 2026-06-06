from game.entities.base import BaseEntity


class GameState:
    def __init__(self, entities: list[BaseEntity] | None = None):
        self.player = player
        self.entities: list[BaseEntity] = entities or []

    def add_entities(self, entities: BaseEntity):
        self.entities.append(entities)