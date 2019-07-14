# Sprite classes.
import pygame

import src.game.settings as s
vector = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    __slots__ = ['groups', 'game', 'image', 'rect', 'vx', 'vy', 'x', 'y']

    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((s.TILE_SIZE, s.TILE_SIZE))
        self.image.fill(s.RED)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * s.TILE_SIZE
        self.y = y * s.TILE_SIZE

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -s.PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = s.PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vy = -s.PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vy = s.PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= s.PLAYER_SPEED_DIAGONAL
            self.vy *= s.PLAYER_SPEED_DIAGONAL

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.width
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
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
