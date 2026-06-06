import numpy
import pygame
from moviepy import VideoFileClip
from pygame import display
from pygame.time import Clock

import constants
from game.core.event_handler import EventHandler
from game.core.monster_spawner import MonsterSpawner
from game.entities.errors import TheEndError
from game.entities.game import Game
from game.entities.game_state import GameState
from game.entities.player import Player
from game.entities.station import Station
from game.entities.task import Task
from game.entities.timer import Timer


def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode(constants.SCREEN_SIZE)
    pygame.display.set_caption("Прилёт")
    return screen


def show_splash_screen(screen, path_video):
    clip = VideoFileClip(path_video)

    for frame in clip.iter_frames(fps=clip.fps):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        surface = pygame.surfarray.make_surface(numpy.transpose(frame, (1, 0, 2)))

        screen.blit(surface, (0, 0))
        pygame.display.flip()
        Clock().tick(clip.fps)


def run_game():
    screen = init_pygame()
    show_splash_screen(screen=screen, path_video="assets/splash_screen.mp4")

    player = Player()
    station = Station()
    timer = Timer()
    task = Task()
    monster_spawner = MonsterSpawner()

    game_state = GameState(player=player, station=station, timer=timer, task=task)
    event_handler = EventHandler(game_state)
    game = Game(game_state)
    clock = Clock()

    try:
        while True:
            clock.tick(60)
            event_handler.handle_events(events=pygame.event.get())
            game.update(game_state=game_state)
            monster_spawner.spawn_monster(game_state=game_state)
            game.render(screen=screen)
            display.flip()
    except TheEndError:
        show_splash_screen(screen=screen, path_video="assets/finish_1920x1080.mp4")


if __name__ == "__main__":
    run_game()
