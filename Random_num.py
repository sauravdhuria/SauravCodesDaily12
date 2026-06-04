import numpy as np
rng =np.random.default_rng()

print(rng.integers(low=1,high=100 ,size=(2,3)))

rng =np.random.default_rng()
print(rng.integers(low=1,high=100 ,size=(2,3)))


print(np.random.uniform(low=1,high=100 ,size=(2,3)))



array=np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)