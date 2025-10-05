import pygame

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
            if event.unicode.isDigit():
                number = int(event.unicode)
                print(f"TODO: load level {number}")

    @classmethod
    def draw(self, game):
        game.screen.fill((0, 0, 0))

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
