import logging

import pygame
from pygame.event import Event

from game.entities.game_state import GameState


class EventHandler:
    def __init__(self, game_state: GameState):
        self.game_state = game_state
        self.key_is_down = False

    def handle_events(self, events: list[Event]):
        player = self.game_state.player

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.key_is_down = True
            if self.key_is_down:
                if event.key == pygame.K_DOWN:
                    player.move_down()
                if event.key == pygame.K_UP:
                    player.move_up()
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_RIGHT:
                    player.move_right()
            if event.type == pygame.KEYUP:
                self.key_is_down = False
