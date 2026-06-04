import numpy as np
array=np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                [['J','K','L'],['N','O','P'],['Q','R','S']],
                [['T','U','V'],['W','X','F'],['G','H','I']]])
print(array)



word=array[0,1,1]+ array[0,0,0]+array[1,2,1]  #print word EAR
print(word)
#Q)print your name
word1=array[1,2,2]+ array[0,0,0]+array[2,0,1]+array[1,2,1]+array[0,0,0]+array[2,0,2]
print(word1)