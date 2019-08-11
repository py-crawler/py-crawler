# Builtins
import sys
from os import path

# Pip
import pygame

# locals
import src.game.settings as s
import src.game.sprites as sprites
from src.dungeon.map import Map, Camera


class Game:
    __slots__ = ['screen', 'clock', 'all_sprites', 'walls', 'player',
                 'playing', 'dt', 'running', 'map', 'camera', 'player_image']

    def __init__(self):
        # Initialize game window, etc.
        pygame.init()
        self.screen = pygame.display.set_mode((s.WIDTH, s.HEIGHT))
        pygame.display.set_caption(s.TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        src = path.join(path.dirname(__file__), r'../')
        assets_folder = path.join(src, r'assets/')
        images_folder = path.join(assets_folder, r'images/')

        self.map = Map(path.join(src, r'dungeon/maps/map.txt'))
        self.player_image = pygame.image.load(path.join(images_folder, r'sprites/human.png')).convert_alpha()

    def new(self):
        # Start a new game.
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    sprites.Wall(self, col, row)
                if tile.lower() == 'p':
                    self.player = sprites.Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # Game loop.
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(s.FPS) / 1000
            self.events()
            self.update()
            self.draw()

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()

    def update(self):
        # Game loop - Update.
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, s.WIDTH, s.TILE_SIZE):
            pygame.draw.line(self.screen, s.LIGHT_GREY, (x, 0), (x, s.HEIGHT))
        for y in range(0, s.HEIGHT, s.TILE_SIZE):
            pygame.draw.line(self.screen, s.LIGHT_GREY, (0, y), (s.WIDTH, y))

    def draw(self):
        # Game loop - draw.
        self.screen.fill(s.BG_COLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
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

    def show_start_screen(self):
        # Start screen.
        pass

    def show_go_screen(self):
        # Show game over/continue screen.
        pass
