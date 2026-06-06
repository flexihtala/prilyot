import pygame

from game.core.event_handler import EventHandler
from game.entities.game import Game
from game.entities.game_state import GameState


def run_game():
    game_state = GameState()
    event_handler = EventHandler(game_state)
    game = Game(game_state)

    while True:
        event_handler.handle_events(pygame.event.get())

def main():
    print("Hello from prilyot!")

if __name__ == "__main__":
    main()
    run_game()
