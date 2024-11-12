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


class NeuralNetwork:
  def __init__(self, layers):
      """
      Initializes the network.
      `layers` is a list where each element specifies the number of neurons in that layer.
      """
      self.layers = []
      for i in range(len(layers) - 1):
          layer = []
          input_size = layers[i]
          output_size = layers[i + 1]
          # Initialize each neuron with random weights and a bias
          for _ in range(output_size):
              weights = np.random.rand(input_size)
              bias = np.random.rand()
              layer.append(Neuron(weights, bias))
          self.layers.append(layer)

  def feed_forward(self, inputs):
      """
      Perform the feedforward operation through all layers.
      `inputs` is an array of inputs for the network.
      """
      for layer in self.layers:
          outputs = []
          for neuron in layer:
              outputs.append(neuron.feed_forward(inputs))
          inputs = np.array(outputs)  # output of this layer is the input to the next
      return inputs  # the final layer output

def mse_loss(y_true, y_pred):
  """
    Mean Squared Error loss function
  """
  return ((y_true - y_pred) ** 2).mean()

y_true = np.array([1, 0, 0, 1])
y_pred = np.array([0, 0, 0, 0])

layer_sizes = input("Enter the number of neurons for each layer separated by spaces (e.g., '2 3 1'): ")
layers = [int(size) for size in layer_sizes.split()]

network = NeuralNetwork(layers)

x = np.array([0.5, -0.5])
print("MSE loss:", mse_loss(y_true, y_pred))
print("Network output:", network.feed_forward(x))