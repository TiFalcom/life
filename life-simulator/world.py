from individual import Individual
from elements import Lake, Bush
from utils import random_pair
import random
import math

class World:
    def __init__(self, width, height, 
                 initial_population_size = 10,
                 qty_lakes = 5,
                 qty_bushes = 10,
                 mortality_rate = 0.1):
        self.width = width
        self.height = height
        self.initial_population_size = initial_population_size
        self.individual_width = 5
        self.individual_height = 5
        self.neighbors_distance = 10
        self.qty_lakes = qty_lakes
        self.qty_bushes = qty_bushes
        self.mortality_rate = mortality_rate

    def build(self):
        # lakes
        excluded_points = []

        self.lakes = []
        for _ in range(self.qty_lakes):
            self.lakes.append(
                Lake(self.width, self.height, 50, 50, excluded_points)
            )
            excluded_points += self.lakes[-1].get_area_points()

        # food
        self.bushes = []
        for _ in range(self.qty_bushes):
            self.bushes.append(
                Bush(
                    self.width, self.height, 25, 25, excluded_points
                )
            )
            excluded_points += self.bushes[-1].get_area_points()

        # individuals
        self.individuals = []
        for _ in range(self.initial_population_size):
            x, y = random_pair(excluded_points, 
                               (0, self.width - self.individual_width), 
                               (0, self.height - self.individual_height),
                               self.individual_width,
                               self.individual_height
                              )
            
            self.individuals.append(
                Individual(
                    x,
                    y,
                    self.individual_width,
                    self.individual_height
                )
            )
            excluded_points += self.individuals[-1].get_area_points()
        
        self._map_standard_entities()
        self._map_dynamic_entities()

    def _map_standard_entities(self):
        self.standard_board = [[0 for _ in range(self.height + 1)] for _ in range(self.width + 1)]

        for lake in self.lakes:
            for x, y in lake.get_area_points():
                self.standard_board[x][y] = 'lake'
        
        for bush in self.bushes:
            for x, y in bush.get_area_points():
                self.standard_board[x][y] = 'bush'

    def _map_dynamic_entities(self):
        self.dynamic_entities = [[0 for _ in range(self.height + 1)] for _ in range(self.width + 1)]

        for individual in self.individuals:
            for x, y in individual.get_area_points():
                self.dynamic_entities[x][y] = 'individual'


    def _calculate_fitness(self):
        fitness = [individual.fitness() for individual in self.individuals]
        return fitness

    def _kill_helders(self, deaths_percent):
        # kill based on fitness * age
        fitness = self._calculate_fitness()
        max_fitness = max(fitness)
        inverse_fitness = [abs(fit - max_fitness) + 1 for fit in fitness]
        kill_probability = sorted([(inv_fit * self.individuals[index].age, index) 
                                   for index, inv_fit in enumerate(inverse_fitness)],
                                   reverse=True)
        
        individuals_to_kill = sorted([index for kill_prob, index in kill_probability[:int(deaths_percent*len(self.individuals))]])

        for index, individual in enumerate(individuals_to_kill):
            self.individuals.pop(individual - index)


    def _move_individuals(self):
        for individual in self.individuals:
            # update position
            x = individual.x + random.randint(-1,1) * individual.speed
            y = individual.y + random.randint(-1,1) * individual.speed

            # reapper on other bound
            if x < 0:
                x = self.width - self.individual_width
            elif x + individual.width > self.width:
                x = 0

            if y < 0:
                y = self.height - self.individual_height
            elif y + individual.height > self.height:
                y = 0

            individual.update(x, y)

    def update(self):
        self._kill_helders(0.01)
        self._move_individuals()
        self._map_dynamic_entities()
    
    def _check_neighbors(self):
        # TODO: Verify if it will be used
        # n², shit code
        neighbors = []
        for i, individual1 in enumerate(self.individuals):
            for j, individual2 in enumerate(self.individuals):
                if i != j:
                    # Euclidean
                    distance = math.sqrt(
                        (individual1.x - individual2.x) ** 2 +
                        (individual1.y - individual2.y) ** 2
                    )
                    if distance <= self.neighbors_distance:
                        neighbors.append((individual1, individual2))
                        # single neighbor
                        break
        return neighbors

    def evolve(self):
        # elitism
        

        # check neighbors

        # crossover

        # TODO: mutation

        pass



    def draw(self, screen):
        for lake in self.lakes:
            lake.draw(screen)

        for bush in self.bushes:
            bush.draw(screen)

        for individual in self.individuals:
            individual.draw(screen)