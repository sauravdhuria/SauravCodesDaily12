import numpy as np

array= np.array([[1,2,3,4],
                 [5,6,7,7],
                 [9,10,11,12],
                 [13,14,15,16]])

#array[start:emd:steps]
#print(array[0])  # output [1,2,3,4]          -4
#print(array[1]) #output [5 6 7 7]          -3
#print(array[1]) #output [9,10,11,12]       -2
#print(array[1]) #output [13,14,15,16]   also -1
#ending index is exclusive so if we want index 2 we need to write 3 as end

#print(array[0:3])

#steps here for list(rows) not for element  so if ve use steps as 2
#print(array[0:3:2])    #output [[ 1  2  3  4]
                              #[ 9 10 11 12]]

#print(array[0:])   #select everything upuntill the end

#print(array[::-1])  #reverse the array

"""Now we get into  colunm selection"""
print(array[:,-1])