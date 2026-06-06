import time

from pygame import image, display, transform

from game import constants


class Menu:
    def __init__(self):
        self.background = transform.scale(image.load("assets/menu_background.png").convert_alpha(), constants.SCREEN_SIZE)
        self.should_be_closed = False

    def run_scene_loop(self, screen):
        while not self.should_be_closed:
            screen.blit(self.background, (0, 0))
            display.flip()
