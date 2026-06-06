import pygame
from pygame.event import Event

from game.entities.game_state import GameState


class EventHandler:
    def __init__(self, game_state: GameState):
        self.game_state = game_state


    def handle_events(self, events: list[Event]):
        for event in events:
            if event.type == pygame.KEYDOWN
