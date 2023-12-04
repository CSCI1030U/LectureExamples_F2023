# 11 - Artificial Intelligence

import numpy as np

# basic forward prop calculation
inputs = [0.2, 2.0, 1.3, 2.1]
weights = [
    [0.2, 0.8, -0.5, 1.0], 
    [0.5, -0.91, 0.17, 0.87], 
    [-0.26, -0.27, 0.17, 0.87],
]
biases = [1.2, 1.3, 0.5]

layer_outputs = np.dot(weights, inputs) + biases

print(f'{layer_outputs = }')

class NeuronLayer:
    def __init__(self, weights, biases):
        self._weights = weights 
        self._biases = biases 

    def forward(self, inputs):
        return self.relu(np.dot(self._weights, inputs) + self._biases)

    def relu(self, dot_products):
        # results = []
        # for dot_product in dot_products:
        #     results.append(max(0.0, dot_product))
        # return results
        return np.maximum(0.0, 0.2 * dot_products + 0.1)

layer1 = NeuronLayer(weights = [[0.2, 0.8, -0.5, 1.0], [0.1, -0.91, 0.17, -0.87], [-0.26, -0.27, 0.17, 0.87],], biases = [1.2, 1.3, 0.5])
print(f'{layer1.forward(inputs = [0.2, 2.0, 1.3, 2.1]) = }')