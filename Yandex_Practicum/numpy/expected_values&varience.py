import numpy as np

# The probability that a python's sign will belong to any one of the 4 elements is 1/4.
# We need to add the probabilities of 2 elemental signs (Fire and Earth) in order to get the probability
# of a python weighing 3 kg. For the other elements, the probability stays at 1/4.

weight_probs = {
                '2': 0.25,
                '3': 0.5,
                '5': 0.25
                }

expectation = sum([int(x_i)*weight_probs[x_i] for x_i in weight_probs])
# (E(X))^2
square_of_expectation = expectation ** 2
# E(X^2)
expectation_of_squares = sum([int(x_i)*int(x_i)*weight_probs[x_i] for x_i in weight_probs])

variance = expectation_of_squares - square_of_expectation

print('Expected value:', expectation)
print('Variance:', variance)