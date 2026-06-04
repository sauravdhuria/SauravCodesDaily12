"""
Filtering refers to the process of selecting elements from 
an array that match or filtering the elements that dosent match
"""

import numpy as np
ages = np.array([[31,35,42,24,72],
                 [12,43,42,13,45]])
teenagers=ages[(ages<=18)]
print(f"Teenagers age are {teenagers}")

adults=ages[(ages>=18) & (ages<=24)]

print(f"Adults age are {adults}")

seniors=ages[(ages>=24) & (ages<=72)]
print(f"Senior age are {seniors}")

even=ages[(ages %2 ==0)]
print(f"Even age are {even}")

odd=ages[(ages %2 !=0)]
print(f"odd age are {odd}")
print(type(ages))
print(ages.shape)
print(type(teenagers))