# reshape() usually creates a view of the original array,
# so modifying reshaped array also changes original array.
#
# flatten() creates an independent copy,
# so modifying flattened array does not affect original array.
import numpy as np
x = np.arange(1, 25) # 24 elements

r = x.reshape(4, 6)
r[0, 0] = 999 # modifies original x!
print('x[0]:', x[0]) # same memory → 999
f = x.flatten() # independent copy
f[0] = 0
print('x[0] after flatten change:', x[0]) # still 999