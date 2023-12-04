# 11 - Artificial Intelligence

import numpy as np

# basic forward propagation for a single neuron layer
inputs = [0.1, 0.9, 0.5, 0.8]
weights = [
    [0.2, -0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87],
]
biases = [0.2, 0.8, 0.1]

layer_outputs = np.dot(weights, inputs) + biases 
print(f'{layer_outputs = }')

# class implementation
class NeuronLayer:
    def __init__(self, weights, biases):
        self._weights = weights 
        self._biases = biases 
    
    def forward(self, inputs):
        return self.relu(np.dot(self._weights, inputs) + self._biases)
    
    def relu(self, weighted_sums):
        # results = []
        # for weighted_sum in weighted_sums:
        #     value = 0.2 * weighted_sum + 0.1
        #     results.append(max(0.0, value))
        # return results 
        # return np.maximum(0.0, weighted_sums)
        # scaled rectified linear (relu)
        return np.maximum(0.0, 0.2 * weighted_sums + 0.1)

hidden_layer1 = NeuronLayer(weights = [
    [0.2, -0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87],
], biases = [0.2, 0.8, 0.1])
print(f'{hidden_layer1.forward(inputs = [0.1, 0.9, 0.5, 0.8])}')