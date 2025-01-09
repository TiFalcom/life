import random
import pygame
from utils import random_pair

BLUE = (0, 167, 239)
MAGENTA = (204, 0, 102)
DARK_GREEN = (0, 153, 0)

class Berry:
    def __init__(self, x, y, size):
        self.color = MAGENTA
        self.size = size
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


class Bush:
    def __init__(self, world_width, world_height, width, height, excluded_points, qty_berries=3, berry_size=5):
        self.x, self.y = random_pair(excluded_points, (0, world_width - width), (0, world_height - height), width, height)
        self.height = height
        self.width = width
        self.color = DARK_GREEN
        self.berries = []
        for _ in range(qty_berries):
            self.berries.append(
                Berry(
                    random.randint(self.x, self.x + self.width - berry_size), 
                    random.randint(self.y, self.y + self.height - berry_size), 
                    berry_size
                )
            )

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        for berry in self.berries:
            berry.draw(screen) 

    def get_area_points(self):
        area_points = []
        for i in range(self.x, self.x + self.width + 1):
            for j in range(self.y, self.y + self.height + 1):
                area_points.append((i, j))
        return area_points
        

class Lake:
    def __init__(self, world_width, world_height, width, height, excluded_points):
        self.x, self.y = random_pair(excluded_points, (0, world_width - width), (0, world_height - height), width, height)
        self.height = height
        self.width = width
        self.color = BLUE

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_area_points(self):
        area_points = []
        for i in range(self.x, self.x + self.width + 1):
            for j in range(self.y, self.y + self.height + 1):
                area_points.append((i, j))
        return area_points


