import pygame
from pygame import Rect, Surface, display, image, transform

from game import constants


class Menu:
    ORIGINAL_BACKGROUND_SIZE = (3346, 1882)
    START_BUTTON_RECT = Rect(2440, 1500, 840, 190)

    def __init__(self):
        self.background = transform.scale(
            image.load("assets/menu_background.png").convert_alpha(),
            constants.SCREEN_SIZE,
        )
        self.start_button_rect = self._scale_rect(self.START_BUTTON_RECT)
        self.should_be_closed = False
        self.clock = pygame.time.Clock()

    def run_scene_loop(self, screen: Surface) -> None:
        self.should_be_closed = False
        while not self.should_be_closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and event.button == pygame.BUTTON_LEFT
                    and self.start_button_rect.collidepoint(event.pos)
                ):
                    self.should_be_closed = True

            screen.blit(self.background, (0, 0))
            display.flip()
            self.clock.tick(60)

    def _scale_rect(self, rect: Rect) -> Rect:
        scale_x = constants.SCREEN_SIZE[0] / self.ORIGINAL_BACKGROUND_SIZE[0]
        scale_y = constants.SCREEN_SIZE[1] / self.ORIGINAL_BACKGROUND_SIZE[1]
        return Rect(
            round(rect.x * scale_x),
            round(rect.y * scale_y),
            round(rect.width * scale_x),
            round(rect.height * scale_y),
        )
