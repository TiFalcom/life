import pygame
import random

# TODO: Create an Population, an aggregation of individuals
class Individual:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (random.randint(0, 190), random.randint(0, 100), random.randint(0, 100))
        self.speed = random.randint(5,15)
        self.age = 1
        self._set_chromosome()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self, x, y):
        self.x = x
        self.y = y
        self.age += self.age

    def fitness(self):
        self._fitness = random.randint(0,100)
        return self._fitness

    def _set_chromosome(self):
        # chromosome will define individual skills
        self.chromosome = [
            random.randint(0,1)
            for _ in range(10)
        ]

    def get_area_points(self):
        area_points = []
        for i in range(self.x, self.x + self.width + 1):
            for j in range(self.y, self.y + self.height + 1):
                area_points.append((i, j))
        return area_points
