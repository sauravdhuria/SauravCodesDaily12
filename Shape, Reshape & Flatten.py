import numpy as np
x=np.arange(1,25)
print(x)

a=x.reshape(2,3,4)
print('2×3×4 :',a)

b=x.reshape(4,6)
print('4×6 :', b)


# unknown dimension
c=x.reshape(-1,6)  #unknown row
print('2×auto :', c)

c=x.reshape(2,-1)  #unknown column
print('2×auto :', c)

#Flattern

print('Flattern  :',a.flatten().shape)

print('Ravel  :',a.ravel().shape)

