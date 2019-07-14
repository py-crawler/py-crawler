# Builtins
import sys

# Pip
import pygame

# locals
import src.game.settings as s
import src.game.sprites as sprites


class Game:
    __slots__ = ['screen', 'clock', 'all_sprites', 'walls', 'player', 'playing',
                 'dt', 'running']

    def __init__(self):
        # Initialize game window, etc.
        pygame.init()
        self.screen = pygame.display.set_mode((s.WIDTH, s.HEIGHT))
        pygame.display.set_caption(s.TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        pass

    def new(self):
        # Start a new game.
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.player = sprites.Player(self, 10, 10)
        for x in range(10, 20):
            sprites.Wall(self, x, 5)

    def run(self):
        # Game loop.
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(s.FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # Game loop - Update.
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, s.WIDTH, s.TILESIZE):
            pygame.draw.line(self.screen, s.LIGHTGREY, (x, 0), (x, s.HEIGHT))
        for y in range(0, s.HEIGHT, s.TILESIZE):
            pygame.draw.line(self.screen, s.LIGHTGREY, (0, y), (s.WIDTH, y))

    def draw(self):
        # Game loop - draw.
        self.screen.fill(s.BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pygame.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pygame.K_UP:
                    self.player.move(dy=-1)
                if event.key == pygame.K_DOWN:
                    self.player.move(dy=1)

    def show_start_screen(self):
        # Start screen.
        pass

    def show_go_screen(self):
        # Show game over/continue screen.
        pass
