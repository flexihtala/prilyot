import logging

import pygame
from pygame.event import Event

from game.entities.game_state import GameState

logger = logging.getLogger(__name__)


class EventHandler:
    def __init__(self, game_state: GameState):
        self.game_state = game_state

    def handle_events(self, events: list[Event]):
        player = self.game_state.player

        for event in events:
            logger.info(f"Тип event: {event.type}")
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.K_DOWN:
                player.move_up()
            if event.type == pygame.K_UP:
                player.move_down()
            if event.type == pygame.K_LEFT:
                player.move_left()
            if event.type == pygame.K_RIGHT:
                player.move_right()
