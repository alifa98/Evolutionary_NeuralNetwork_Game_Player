import numpy as np


class NeuralNetwork():

    def __init__(self, layer_sizes):

        # layer_sizes example: [4, 10, 2]
        self.biases = [np.random.randn(y, 1) for y in layer_sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(layer_sizes[:-1], layer_sizes[1:])]

    def activation(self, x):

        return 1.0/(1.0 + np.exp(-x))

    def forward(self, x):

        # x example: np.array([[0.1], [0.2], [0.3]])
        output = x
        for b, w in zip(self.biases, self.weights):
            output = self.activation(np.dot(w, output) + b)
        return output
