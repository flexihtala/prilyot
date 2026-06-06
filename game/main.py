import pygame
from pygame import display
from pygame.time import Clock
from game.core.event_handler import EventHandler
from game.entities.game import Game
from game.entities.game_state import GameState
from game.entities.monster import Monster
from game.entities.player import Player
from game.entities.station import Station
from game.entities.timer import Timer


def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("Прилёт")
    return screen


def run_game():
    screen = init_pygame()

    player = Player()
    station = Station()
    timer = Timer()
    monster1 = Monster([200, 0])
    monster2 = Monster([500, 250])
    monster3 = Monster([300, 500])
    game_state = GameState(player=player, station=station, timer=timer)
    game_state.add_monster(monster1)
    game_state.add_monster(monster2)
    game_state.add_monster(monster3)
    event_handler = EventHandler(game_state)
    game = Game(game_state)

    while True:
        Clock().tick(60)
        screen.fill((0, 0, 0))
        event_handler.handle_events(pygame.event.get())
        game.update()
        game.render(screen)
        display.flip()


def main():
    print("Hello from prilyot!")


if __name__ == "__main__":
    main()
    run_game()
