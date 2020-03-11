import numpy as np 

A = np.array([[1,1,1],[0,2,5],[2,5,-1]])# 初始化A矩阵
print('矩阵A：') 
print(A)

A_inv = np.linalg.inv(A)# 求A的逆
print('A的逆：')
print(A_inv)

print('向量b：')
b = np.array([3,-2,13.5]).reshape(-1,1)# 初始化向量b
print(b)

print('求解x：')
x = np.dot(A_inv,b)# 求解x
print(x)