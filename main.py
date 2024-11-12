import numpy as np
from neural_network import NeuralNetwork

def mse_loss(y_true, y_pred):
    """Mean Squared Error loss function"""
    return ((y_true - y_pred) ** 2).mean()


# Example usage
y_true = np.array([1, 0, 0, 1])
y_pred = np.array([0, 0, 0, 0])

layer_sizes = input("Enter the number of neurons for each layer separated by spaces (e.g., '2 3 1'): ")
layers = [int(size) for size in layer_sizes.split()]

network = NeuralNetwork(layers)

x = np.array([-0.5])  # Single input value

print("MSE loss:", mse_loss(y_true, y_pred))
print("Network output:", network.feed_forward(x))