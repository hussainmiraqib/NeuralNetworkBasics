"""
README

This script demonstrates a basic implementation of the softmax function,
which is commonly used in machine learning, particularly in the context of
neural networks.

The softmax function converts a vector of values (in this case, the outputs
of a neural network layer) into a probability distribution. The sum of all
probabilities in this distribution will be equal to 1.

The process consists of the following steps:
1. Import the necessary math module.
2. Define the input vector `layer_outputs`, which represents the output values
   from a neural network layer.
3. Define the mathematical constant e (Euler's number) using the `math` module.
4. Calculate the exponential values for each element in `layer_outputs`.
5. Normalize these exponential values to get the probabilities by dividing each
   exponential value by the sum of all exponential values.
6. Print the exponential values, the normalized values, and the sum of the
   normalized values (which should be 1).

Code Explanation:
1. `import math`: Imports the math module for mathematical functions.
2. `layer_outputs = [4.8, 1.21, 2.385]`: Initializes the input vector with
   three example output values.
3. `E = math.e`: Sets the variable `E` to Euler's number.
4. `exp_values = []`: Initializes an empty list to store the exponential values.
5. `for output in layer_outputs: exp_values.append(E**output)`: Iterates through
   `layer_outputs`, calculates the exponential of each value, and stores it in
   `exp_values`.
6. `print(exp_values)`: Prints the list of exponential values.
7. `norm_base = sum(exp_values)`: Calculates the sum of the exponential values.
8. `norm_values = []`: Initializes an empty list to store the normalized values.
9. `for value in exp_values: norm_values.append(value / norm_base)`: Iterates
   through `exp_values`, normalizes each value by dividing it by `norm_base`,
   and stores it in `norm_values`.
10. `print(norm_values)`: Prints the list of normalized values.
11. `print(sum(norm_values))`: Prints the sum of the normalized values, which
    should be 1.

"""