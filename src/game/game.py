# Builtins
import sys
from os import path

# Pip
import pygame

# locals
import src.game.settings as s
import src.game.sprites as sprites


class Game:
    __slots__ = ['screen', 'clock', 'all_sprites', 'walls', 'player', 'playing',
                 'dt', 'running', 'map_data']

    def __init__(self):
        # Initialize game window, etc.
        pygame.init()
        self.screen = pygame.display.set_mode((s.WIDTH, s.HEIGHT))
        pygame.display.set_caption(s.TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.join(path.dirname(__file__), r'../dungeon/maps')
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        # Start a new game.
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    sprites.Wall(self, col, row)
                if tile.lower() == 'p':
                    self.player = sprites.Player(self, col, row)

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
        for x in range(0, s.WIDTH, s.TILE_SIZE):
            pygame.draw.line(self.screen, s.LIGHT_GREY, (x, 0), (x, s.HEIGHT))
        for y in range(0, s.HEIGHT, s.TILE_SIZE):
            pygame.draw.line(self.screen, s.LIGHT_GREY, (0, y), (s.WIDTH, y))

    def draw(self):
        # Game loop - draw.
        self.screen.fill(s.BG_COLOR)
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
