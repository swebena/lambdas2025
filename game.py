import pygame
from settings import WIDTH, HEIGHT, FPS
import activities

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.running = True
        self.currentActivity = activities.MainMenuActivity

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.currentActivity.handle_pygame_event(event)

    def update(self):
        self.currentActivity.update(game)

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.currentActivity.draw(game)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
