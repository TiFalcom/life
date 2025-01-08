from individual import Individual
import random
import math

class World:
    def __init__(self, height, width, 
                 initial_population_size = 10):
        self.height = height
        self.width = width
        self.initial_population_size = initial_population_size
        self.individual_size = 5
        self.neighbors_distance = 10

    def build(self):
        self.individuals = [
            Individual(
                random.randint(0, self.width - 20),
                random.randint(0, self.height - 20),
                self.individual_size
            )
            for _ in range(self.initial_population_size)
        ]

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
                x = self.width
            elif x + individual.size > self.width:
                x = 0

            if y < 0:
                y = self.height
            elif y + individual.size > self.height:
                y = 0

            individual.update(x, y)

    def update(self):
        self._kill_helders(0.1)
        self._move_individuals()
    
    def _check_neighbors(self):
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
        for individual in self.individuals:
            individual.draw(screen)