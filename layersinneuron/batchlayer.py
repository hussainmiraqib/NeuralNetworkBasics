import numpy as np 

# Set a seed for the random number generator to ensure reproducibility
np.random.seed(0)

# Input data (3 samples, each with 4 features)
X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]

# Define a class for a dense layer in the neural network
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        # Initialize weights with small random values and biases with zeros
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        
    def forward(self, inputs):
        # Calculate the output of the layer by performing a dot product of inputs and weights, and adding biases
        self.output = np.dot(inputs, self.weights) + self.biases

# Create the first dense layer with 4 inputs and 5 neurons
layer1 = Layer_Dense(4,5)
# Create the second dense layer with 5 inputs and 2 neurons
layer2 = Layer_Dense(5,2)

# Perform a forward pass of the first layer using the input data
layer1.forward(X)
# Print the output of the first layer
print("layer1 output")
print(layer1.output)
print()

# Perform a forward pass of the second layer using the output of the first layer
layer2.forward(layer1.output)
# Print the output of the second layer
print("layer2 output")
print(layer2.output)

'''
Diagram:

          Input Layer
        (4 input features)
        [1, 2, 3, 2.5]
        [2.0, 5.0, -1.0, 2.0]
        [-1.5, 2.7, 3.3, -0.8]
               |
               v
---------------------------------
|                               |
|       Dense Layer 1           |
|        (5 neurons)            |
|                               |
---------------------------------
|    |    |    |    |           |
| N1 | N2 | N3 | N4 | N5        |
|    |    |    |    |           |
---------------------------------
               |
               v
---------------------------------
|                               |
|       Dense Layer 2           |
|        (2 neurons)            |
|                               |
---------------------------------
|    |                          |
| N1 | N2                       |
|    |                          |
---------------------------------
               |
               v
             Output
            (2 values)
'''
