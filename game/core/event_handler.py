
import pygame
from pygame.event import Event

from game.entities.game_state import GameState


class EventHandler:
    def __init__(self, game_state: GameState):
        self.game_state = game_state
        self.key_is_down = False
        self.set_keys: set[int] = set()
        self.registered_keys: set[int] = {
            pygame.K_DOWN,
            pygame.K_UP,
            pygame.K_LEFT,
            pygame.K_RIGHT,
        }

    def handle_events(self, events: list[Event]):
        player = self.game_state.player

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key in self.set_keys:
                    self.set_keys.remove(event.key)

            if event.type == pygame.KEYDOWN and event.key in self.registered_keys:
                self.set_keys.add(event.key)

        for key in self.set_keys:
            match key:
                case pygame.K_DOWN:
                    player.move_down()
                case pygame.K_UP:
                    player.move_up()
                case pygame.K_LEFT:
                    player.move_left()
                case pygame.K_RIGHT:
                    player.move_right()
