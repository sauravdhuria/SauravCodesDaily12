# Broadcasting:
# NumPy automatically expands smaller arrays to match
# the shape of larger arrays during arithmetic operations.
#
# Here:
# x has shape (2,3)
# y has shape (3,)
#
# NumPy broadcasts y across each row of x.
#
# Element-wise multiplication:
# [1 2 3] * [100 200 300]
# [4 5 6] * [100 200 300]
#
# np.dot(x, y):
# Performs matrix multiplication (dot product)
# between rows of x and vector y.
import numpy as np


x=np.array([[1,2,3],[4,5,6]])

print(f'x : {x}' )

y=np.array([100,200,300])

print(f'y : {y}' )

print(f'x  * y : {(x*y)}' )

print(f'dot function: {(np.dot(x,y))}' )