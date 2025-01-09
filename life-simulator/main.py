import pygame
from time import sleep
from world import World
from yaml import safe_load
from helper import plot_fitness


# setup variables
setup_vars = safe_load(open('config.yml', 'r'))
locals().update(setup_vars)

# Inicializa o Pygame
pygame.init()
screen = pygame.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT))
pygame.display.set_caption("Simulação de Indivíduos")

# Define as cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRASS = (153, 255, 102)

# Loop principal
running = True
world = World(WORLD_WIDTH, WORLD_HEIGHT, 
              INITIAL_POPULATION_SIZE, QTY_LAKES, QTY_BUSHES, 
              MORTALITY_RATE)
world.build()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche a tela com branco
    screen.fill(GRASS)
    world.draw(screen)
    
    # Atualiza a tela
    pygame.display.flip()
    world.update()
    plot_fitness(world._calculate_fitness())
    #sleep(UPDATE_SLEEP)


# Finaliza o Pygame
pygame.quit()
