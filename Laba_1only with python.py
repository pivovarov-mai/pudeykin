#!/usr/bin/env python
# coding: utf-8

# In[23]:


m=([[-5,-1,-3,-1,18],
         [-2,0,8,-4,-12],
         [-7,-2,2,-2,6],
         [2,-4,-4,4,-12]])
def max_row(m, index):

    max_element = m[index][index]
    max_row = index
    for i in range(index + 1, len(m)):
        if abs(m[i][index]) > abs(max_element):
            max_element = m[i][index]
            max_row = i
    if max_row != index:
        m[index], m[max_row] = m[max_row], m[index]


def gauss(m):

    n = len(m)
    for k in range(n - 1):  #прямой ход
        max_row(m, k)
        for i in range(k + 1, n):
            div = m[i][k] / m[k][k]
            m[i][-1] -= div * m[k][-1]
            for j in range(k, n):
                m[i][j] -= div * m[k][j]

    if singular(m):
        print('Система имеет бесконечное количество ответов')
        return

    # backward trace
    x = [0 for i in range(n)]
    for k in range(n - 1, -1, -1):
        x[k] = (m[k][-1] - sum([m[k][j] * x[j] for j in range(k + 1, n)])) / m[k][k]
    print(x)


def singular(m):

    for i in range(len(m)):
        if not m[i][i]:
            return True
    return False
gauss(m)


# In[ ]:





# In[ ]:




