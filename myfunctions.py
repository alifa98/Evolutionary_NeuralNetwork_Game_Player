import random
from player import Player
import numpy as np
from math import floor
from operator import attrgetter


def tournament_selection(population, q):
    selected = random.choices(population, k=q)
    parents = sorted(selected, key=lambda agent: agent.fitness, reverse=True)
    return parents[0]


def save_population_info(population, filename):

    maximum = population[0].fitness
    minimum = population[0].fitness
    average = 0
    for item in population:
        average = average + item.fitness
        maximum = item.fitness if item.fitness > maximum else maximum
        minimum = item.fitness if item.fitness < minimum else minimum

    average = average/len(population)

    name = "hist/evol_history-"+filename+".csv"
    with open(name, 'a') as file:
        file.write(str(maximum)+","+str(average)+","+str(minimum)+"\n")


def crossover(parent1, parent2, rate):

    p1_biases = parent1.nn.biases
    p2_biases = parent2.nn.biases

    p1_weights = parent1.nn.weights
    p2_weights = parent2.nn.weights

    child1_biases = []
    child2_biases = []

    child1_weights = []
    child2_weights = []

    if rate > random.random():
        for u, v in zip(p1_biases, p2_biases):
            cross_point = floor(u.shape[0] / 2)
            child1_biases.append(np.concatenate((u[0:cross_point], v[cross_point:]), axis=0))
            child2_biases.append(np.concatenate((v[0:cross_point], u[cross_point:]), axis=0))

        for u, v in zip(p1_weights, p2_weights):
            cross_point = floor(u.shape[0] / 2)  # cross over from middle of matrix
            child1_weights.append(np.concatenate((u[0:cross_point], v[cross_point:]), axis=0))
            child2_weights.append(np.concatenate((v[0:cross_point], u[cross_point:]), axis=0))

    else:
        child1_biases = [x.copy() for x in p1_biases]
        child2_biases = [x.copy() for x in p2_biases]
        child1_weights = [x.copy() for x in p1_weights]
        child2_weights = [x.copy() for x in p2_weights]

    child1 = Player(mode=parent1.mode)
    child1.nn.biases = child1_biases
    child1.nn.weights = child1_weights

    child2 = Player(mode=parent2.mode)
    child2.nn.biases = child2_biases
    child2.nn.weights = child2_weights

    return child1, child2


def sus(population, n):
    fitnesses = [agent.fitness for agent in population]
    sum_fitness = sum(fitnesses)
    probabilities = [x / sum_fitness for x in fitnesses]
    return np.random.choice(population, p=probabilities, size=n, replace=False).tolist()


def top_k_selection(population, k):
    items = sorted(population, key=lambda agent: agent.fitness, reverse=True)
    return items[:k]
