import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot_fitness(fitness_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()

    plt.title('Fitness')
    plt.xlabel('Individuals')
    plt.ylabel('Fitness')

    individuals = list(range(len(fitness_scores)))
    plt.bar(individuals, fitness_scores, color='skyblue')

    for i, score in enumerate(fitness_scores):
        plt.text(i, score + 0.5, str(score), ha='center', va='bottom', fontsize=8)

    plt.show(block=False)
    plt.pause(0.1)
