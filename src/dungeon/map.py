# Pip
import pygame

# locals
import src.game.settings as s


class Map:
    __slots__ = ['data', 'tile_width', 'tile_height', 'width', 'height']

    def __init__(self, filename: str = 'map.txt'):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                if line[0] == '#':
                    continue
                self.data.append(line.strip())

        self.tile_width = len(self.data[0])
        self.tile_height = len(self.data)
        self.width = self.tile_width * s.TILE_SIZE
        self.height = self.tile_height * s.TILE_SIZE


class Camera:
    __slots__ = ['camera', 'width', 'height']

    def __init__(self, width: int, height: int):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity) -> pygame.Rect:
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(s.WIDTH / 2)
        y = -target.rect.y + int(s.HEIGHT / 2)

        # Limit scrolling to map size.
        # TODO: add a small border around the game 2-5 tiles.
        x = min(0, x)  # Left
        y = min(0, y)  # Right
        x = max(-(self.width - s.WIDTH), x)  # Right
        y = max(-(self.height - s.HEIGHT), y)  # Bottom
        self.camera = pygame.Rect(x, y, self.width, self.height)
