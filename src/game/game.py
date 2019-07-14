import pygame
from src.game.settings import *
from src.game.sprites import *


class Game:
    __slots__ = ['running', 'screen', 'clock', 'playing', 'all_sprites',
                 'player', 'platforms']

    def __init__(self):
        # Initialize game window, etc.
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITTLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False

    def new(self):
        # Start a new game.
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        p1 = Platform(0, HEIGHT - 40, WIDTH, 40)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        p2 = Platform(WIDTH /2 - 50, HEIGHT * 3 / 4, 100, 20)
        self.all_sprites.add(p2)
        self.platforms.add(p2)
        self.run()

    def run(self):
        # Game loop.
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop - Update.
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.position.y = hits[0].rect.top
            self.player.velocity.y = 0

    def events(self):
        # Game loop - events.
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game loop - draw.
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    def show_start_screen(self):
        # Start screen.
        pass

    def show_go_screen(self):
        # Show game over/continue screen.
        pass
