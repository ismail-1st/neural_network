import numpy as np

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def sigmoid(self, x):
        """Activation function: f(x) = 1 / (1 + e^(-x))"""
        return 1 / (1 + np.exp(-x))

    def feed_forward(self, inputs):
        """Compute the output by performing the dot product and applying the sigmoid function."""
        total = np.dot(self.weights, inputs) + self.bias
        return self.sigmoid(total)