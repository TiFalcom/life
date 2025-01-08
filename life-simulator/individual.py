import pygame
import random

BLUE = (0, 0, 255)

class Individual:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed = random.randint(5,15) # size
        self.age = 1
        self._set_chromosome()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

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
