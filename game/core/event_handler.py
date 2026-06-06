import pygame
from pygame.event import Event
from game.constants import MAX_TEXT_LEN

from game.entities.enums import TaskStatus
from game.entities.game_state import GameState

class EventHandler:
    def __init__(self, game_state: GameState):
        self.game_state = game_state
        self.key_is_down = False
        self.set_keys: set[int] = set()
        self.is_mouse_button_pressed = False
        self.mouse_pos: list[int] = [0, 0]
        self.registered_keys: set[int] = {
            pygame.K_DOWN,
            pygame.K_UP,
            pygame.K_LEFT,
            pygame.K_RIGHT,
            pygame.K_e,
        }

    def handle_events(self, events: list[Event]):
        player = self.game_state.player
        station = self.game_state.station
        task = self.game_state.task

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key in self.set_keys:
                    self.set_keys.remove(event.key)

                if task.status is TaskStatus.open:
                    if event.key == pygame.K_BACKSPACE:
                        task.current_text = task.current_text[:-1]

                    elif event.key == pygame.K_RETURN:
                        task.status = TaskStatus.enter

                    else:
                        if len(task.current_text) <= MAX_TEXT_LEN:
                            task.current_text += event.unicode
            if event.type == pygame.MOUSEBUTTONUP and self.is_mouse_button_pressed:
                self.is_mouse_button_pressed = False
                self.game_state.player.shooter.frame_counter = -1

                if event.key == pygame.K_e and player.is_near_station(station):
                    task.status = TaskStatus.open

            if event.type == pygame.KEYDOWN and event.key in self.registered_keys:
                self.set_keys.add(event.key)

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_mouse_button_pressed = True

            self.mouse_pos = list(pygame.mouse.get_pos())


        for key in self.set_keys:
            if task.status is not TaskStatus.open:
                match key:
                    case pygame.K_DOWN:
                        player.move_down()
                    case pygame.K_UP:
                        player.move_up()
                    case pygame.K_LEFT:
                        player.move_left()
                    case pygame.K_RIGHT:
                        player.move_right()

        if self.is_mouse_button_pressed:
            player.shoot(self.game_state, self.mouse_pos)
