#!/usr/bin/env python
# coding: utf-8

# In[13]:


from numpy import  zeros
a = [[18, -9, 0, 0, 0],
         [2, -9, -4, 0, 0],
         [0, -9, 21,-8, 0],
         [0, 0, -4, -10, 5],
         [0, 0, 0, 7, 12]]
b = [-81,71, -39, 64, 3]
n=5
x = zeros(n)

#Прямой ход
m = 1
for i in range(1,n):
    m = a[i][i - 1]/a[i-1][i-1] 
    a[i][i] = a[i][i] - m*a[i-1][i] 
    b[i] = b[i] - m*b[i-1] 

#Обратный ход
x[n-1] = b[n-1]/a[n-1][n-1];
for i in range(n - 2, -1, -1):
    x[i]=(b[i] - a[i][i + 1]*x[i+1]) / a[i][i]

print(x)


# In[ ]:





# In[ ]:




