# Sprite classes.
import pygame

from src.game.settings import *
vector = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    __slots__ = ['image', 'rect', 'position', 'velocity', 'acceleration']

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.position = vector(WIDTH / 2, HEIGHT / 2)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)

    def update(self):
        self.acceleration = vector(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -PLAYER_ACCELERATION
        if keys[pygame.K_RIGHT]:
            self.acceleration.x = PLAYER_ACCELERATION

        # Apply friction.
        self.acceleration.x += self.velocity.x * PLAYER_FRICTION
        # Equations of motion.
        self.velocity += self.acceleration
        self.position += self.velocity + .5 * self.acceleration
        # Wrap around the sides of the screen.
        if self.position.x > WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = WIDTH

        self.rect.midbottom = self.position


class Platform(pygame.sprite.Sprite):
    __slots__ = ['image', 'rect', ]

    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
