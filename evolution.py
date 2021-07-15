from player import Player
import numpy as np
from config import CONFIG
from myfunctions import crossover, sus, top_k_selection, tournament_selection


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        # child: an object of class `Player`

        biases = child.nn.biases
        weights = child.nn.weights

        for i in range(len(biases)):
            if(CONFIG["mutaion_rate"] > np.random.rand()):
                child.nn.biases[i] = child.nn.biases[i] + np.random.normal(CONFIG["mutation_mean"], CONFIG["mutation_standard_deviation"], size=biases[i].shape)

        for i in range(len(weights)):
            if(CONFIG["mutaion_rate"] > np.random.rand()):
                child.nn.weights[i] = child.nn.weights[i] + np.random.normal(CONFIG["mutation_mean"], CONFIG["mutation_standard_deviation"], size=weights[i].shape)

    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # num_players example: 150
            # prev_players: an array of `Player` objePcts

            # (additional): a selection method other than `fitness proportionate`
            # q-tournoment selection (Q = 2) (due to mu+lambda method)
            selected_references = []
            for _ in range(num_players):
                selected_references.append(tournament_selection(prev_players, 2))

            # (additional): implementing crossover
            paired_parents = zip(selected_references[::2], selected_references[1::2])
            selected_clone = []
            for parent1, parent2 in paired_parents:
                children = crossover(parent1, parent2, CONFIG["crossover_rate"])
                [selected_clone.append(i) for i in children]

            # mutation
            for i in range(len(selected_clone)):
                self.mutate(selected_clone[i])

            return selected_clone

    def next_population_selection(self, players, num_players):

        # num_players example: 100
        # players: an array of `Player` objects

        # (additional): a selection method other than `top-k`
        # stocastic selection sampling

        selected = []
        if(CONFIG["SUS_in_next_population"]):
            selected = sus(players, num_players)
        else:
            selected = top_k_selection(players, num_players)

        # (additional): plotting
        # TODO: the save information fucntion is written in functions.py

        return selected
