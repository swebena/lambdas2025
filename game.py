import pygame
from settings import WIDTH, HEIGHT, FPS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
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
                    print("Escape pressed - exiting")

    def update(self):
        # TODO: logic
        pass

    def draw(self):
        self.screen.fill((30, 30, 30))
        # TODO: draw game objects
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
