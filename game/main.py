import pygame

from game.core.event_handler import EventHandler
from game.entities.game import Game
from game.entities.game_state import GameState
from game.entities.player import Player
from game.entities.station import Station
from game.entities.timer import Timer


def init_pygame():
    pygame.init()
    pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Прилёт")


def run_game():
    init_pygame()

    player = Player()
    station = Station()
    timer = Timer()
    game_state = GameState(player=player, station=station, timer=timer)
    event_handler = EventHandler(game_state)
    game = Game(game_state)

    while True:
        event_handler.handle_events(pygame.event.get())
        game.update()
        game.render()


def main():
    print("Hello from prilyot!")


if __name__ == "__main__":
    main()
    run_game()
