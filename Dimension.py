import numpy as np
#
# array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
#                   [['J','K','L'],['M','N','O'],['P','Q','R']],
#                   [['S','T','U'],['V','W','X'],['Y','Z','']]])
#
# print(array.shape)

# a=np.array(10)
#
# print("ndim :" ,a.ndim)
# print("shape :" ,a.shape)
# print("size :" ,a.size)
# print("dtype :" ,a.dtype)

# b= np.array([10,20,30,40,50])
#
# print("ndim :" ,b.ndim)
# print("shape :" ,b.shape)
# print("size :" ,b.size)
# print("dtype :" ,b.dtype)
# print(b[1])
# print(b[0])

# even=np.arange(2,22,2)
# print(even)

# even_2d=even.reshape(2,5)
# print(even_2d)
# print(even_2d[::,:1:])
# print("shape :" ,even_2d.shape)
# print("size :" ,even_2d.size)
# print(even_2d[:,:3])

# print(even_2d[-1::-1])



# marks = np.array([[78, 85, 92],
#                 [60, 74, 55],
#                 [88, 91, 87],
#                 [45, 50, 60],
#                 [95, 89, 76]])
# total=(marks.sum(axis=1))
#
# print(marks.sum(axis=1))
# print(marks.mean(axis=0))
# print(np.argmax(total))


# t=np.array([[[1,2,3],
#               [4,5,6]],
#              [[7,8,9],
#              [10,11,12],]])
# print(t)
#
# print(t.shape)
# print(t[:,1,1])

np.random.seed(0)
img = np.random.randint(0, 256, size=(2, 3, 3), dtype=np.uint8)
print('Image shape:', img.shape)
print('Red channel:\n', img[:, :, 0])
img_no_blue = img.copy()
img_no_blue[:, :, 2] = 0
print('Blue channel after zeroing:\n', img_no_blue[:, :, 2])