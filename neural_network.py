import numpy as np
from neuron import Neuron

class NeuralNetwork:
    def __init__(self, layers):
        """
        Initializes the network.
        `layers` is a list where each element specifies the number of neurons in that layer.
        """
        self.layers = []
        # Start with a single input value (could be dynamic)
        self.input_size = 1  # You can change this to match user input
        
        for i in range(len(layers) - 1):
            layer = []
            input_size = layers[i]  # Number of neurons in the current layer (input to the next layer)
            output_size = layers[i + 1]  # Number of neurons in the next layer
            
            # Adjust the input size based on the user-provided layers
            if i == 0:
                self.input_size = input_size  # First layer takes the input_size as its input
                
            # Initialize each neuron with random weights and a bias
            for _ in range(output_size):
                weights = np.random.rand(input_size)  # Weights size should match the input size
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