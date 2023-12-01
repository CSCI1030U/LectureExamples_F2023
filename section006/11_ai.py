# 11 - Artificial Intelligence

import numpy as np

# basic calculation
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.9, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87],
]
biases = [2.0, 3.0, 0.5]
layer_outputs = np.dot(weights, inputs) + biases
print(f'{layer_outputs = }')

# class implementation
class NeuronLayer:
    def __init__(self, weights, biases):
        self._weights = weights 
        self._biases = biases 
    
    def forward(self, inputs):
        return self.relu_scaled(np.dot(self._weights, inputs) + self._biases)
    
    # activation functions
    def relu(self, input):
        return np.max(0.0, input)
    
    def relu_scaled(self, inputs):
        # results = []
        # for input in inputs:
        #     results.append(max(0.0, 0.2 * input + 0.5))
        # return results
        return np.maximum(0.0, 0.2 * inputs + 0.5)

layer = NeuronLayer(weights = [[0.2, -0.8, -0.5, -1.0],[0.5, -0.9, 0.26, -0.5],[-0.26, -0.27, 0.17, 0.87]], biases = [0.0, 3.0, 0.5])
print(f'{layer.forward(inputs = [1.0, 2.0, 3.0, 2.5]) = }')
