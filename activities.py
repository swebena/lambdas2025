import pygame
import sys
from helpers.font_scrappy import draw_text

MAIN_MENU_ACTIVITY = 1
GAME_ACTIVITY = 2

class Activity:
    def draw(self, game):
        pass
    def update(self, game):
        pass
    def handle_pygame_event(self, event):
        pass

class MainMenuActivity(Activity):
    def __init__(self):
        super().__init__()

    @classmethod
    def handle_pygame_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.unicode.isdigit():
                number = int(event.unicode)
                print(f"TODO: load level {number}")
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    @classmethod
    def update(self, game):
        pass

    @classmethod
    def draw(self, game):
        start = (40, 40)
        lines = [
                "<Untitled Project>",
                "Press a number to play the respective level",
                "Q to quit",
                ]
        game.screen.fill((0, 0, 0))
        for i, line in enumerate(lines):
            draw_text(game.screen, line, 80, 90*(i+1))

class GameActivity(Activity):
    def __init__(self):
        super().__init__()

    @classmethod
    def draw(self, game):
        game.screen.fill((0, 0, 0))

    @classmethod
    def handle_pygame_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("W pressed - move up")
            elif event.key == pygame.K_a:
                print("A pressed - move left")
            elif event.key == pygame.K_s:
                print("S pressed - move down")
            elif event.key == pygame.K_d:
                print("D pressed - move right")
            elif event.key == pygame.K_SPACE:
                print("Space pressed - jump/shoot/etc.")
            elif event.key == pygame.K_ESCAPE:
                game.currentActivity = MainMenuActivity
                print("Escape pressed - exiting to main menu")
