''' Homework 1 for Math 682

Instructions: fill in the code below following the instructions in the comments.
'''

import numpy as np
from numpy.linalg import matrix_power, eig

# There are 6 age classes: newborns, young juveniles, juveniles, early adults, 
#   middle-age adults, older adults
# Fecundity rates (in that order) are:
F = np.array([0, 0, 0, 5, 2, 0])
# Survival probabilities for each class are:
P = np.array([0.4, 0.6, 0.7, 0.9, 0.8, 0])
# Starting population numbers (time t=0) are:
N0 = np.array([100, 60, 60, 40, 30, 10])

# Create a 6x6 Leslie matrix below. Use np.zeros to create a starting matrix,
#   and then fill in the non-zero entries either with a for-loop or by making
#   use of the matrix structure. DO NOT hardcode an element-by-element assignment
#   of matrix entries!



# Run your model for 100 time steps (time t=100) using matrix-vector multiplication.
#   (Note: you can use matrix_power to do this faster than a for-loop)



# Sum the number of adults, rounding to the nearest integer. Print this number
#   to the terminal.



# Using eig, print the eigenvalues (but leave out the eigenvectors) of the leslie matrix



# Using code, automatically identify which eigenvalue has the largest magnitude
#   (note: they could be complex! np.abs will give you the modulus) and print it 
#   out with a message saying it is the dominant eigenvalue.
# Arrays have a method max() which will give you the max value in the array, and 
#   an argmax method which whill give you the position of the largest value in 
#   the array:
# dom_lam_pos = np.abs(lam).argmax()



# Also using code, detect whether or not the dominant eigenvalue is less than or 
#   greater than one. Using this info, print out a message about the long term 
#   behavior of the population.


