from tkinter import W
import pygame
import random
from time import sleep
from world import World

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simulação de Indivíduos")

# Define as cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Classe para representar um indivíduo

X_INIT = 100
Y_INIT = 100

# Loop principal
running = True
world = World(screen_height, screen_width, 1000)
world.build()
i = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche a tela com branco
    screen.fill(WHITE)
    world.draw(screen)
    
    # Atualiza a tela
    pygame.display.flip()
    world.update()
    sleep(0.1)


# Finaliza o Pygame
pygame.quit()
