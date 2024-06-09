inputs = [1,2,3,2.5]  ## Input here is a vector

weights = [[0.2,0.8,-0.5,1.0],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]]  ## weights is a matrix here 

biases = [2,3,5]  ## this is according to the number of neurons so there are three neurons so there bias values.

import numpy as np
output = np.dot(weights, inputs) + biases

print(output)