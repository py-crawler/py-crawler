# Pip
import pygame

# locals
import src.game.settings as s
vector = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    __slots__ = ['groups', 'game', 'image', 'rect', 'velocity', 'position']

    def __init__(self, game, x: int, y: int):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((s.TILE_SIZE, s.TILE_SIZE))
        self.image.fill(s.RED)
        self.rect = self.image.get_rect()
        self.velocity = vector(x=0, y=0)
        self.position = vector(x=x, y=y) * s.TILE_SIZE

    def get_keys(self):
        self.velocity = vector(x=0, y=0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity.x = -s.PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity.x = s.PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.velocity.y = -s.PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.velocity.y = s.PLAYER_SPEED
        if self.velocity.x != 0 and self.velocity.y != 0:
            self.velocity *= s.PLAYER_SPEED_DIAGONAL

    def collide_with_walls(self, direction: str):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.velocity.x > 0:
                    self.position.x = hits[0].rect.left - self.rect.width
                if self.velocity.x < 0:
                    self.position.x = hits[0].rect.right
                self.velocity.x = 0
                self.rect.x = self.position.x
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.velocity.y > 0:
                    self.position.y = hits[0].rect.top - self.rect.width
                if self.velocity.y < 0:
                    self.position.y = hits[0].rect.bottom
                self.velocity.y = 0
                self.rect.y = self.position.y

    def update(self):
        self.get_keys()
        self.position += self.velocity * self.game.dt
        self.rect.x = self.position.x
        self.collide_with_walls('x')
        self.rect.y = self.position.y
        self.collide_with_walls('y')


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((s.TILE_SIZE, s.TILE_SIZE))
        self.image.fill(s.GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * s.TILE_SIZE
        self.rect.y = y * s.TILE_SIZE
