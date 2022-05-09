#!/usr/bin/env python
# coding: utf-8

# In[4]:


from scipy import linalg
import numpy as np
if __name__ == '__main__':
    # для метода прогонки. 1 над диагональю. И 1 под диагональю
    u = 1
    l = 1
    n = 5
    m = 5
    a = [[18, -9, 0, 0, 0],
         [2, -9, -4, 0, 0],
         [0, -9, 21,-8, 0],
         [0, 0, -4, -10, 5],
         [0, 0, 0, 7, 12]]
    b = [-81,71, -39, 64, 3]
    a = np.array(a)
    b = np.array(b)
    ab = np.zeros((u + l + 1, m))
    for j in range(m):
        for i in range(n):
            index = u + i - j
            if 0 <= index < u + l + 1:
                ab[index][j] = a[i][j]
    ans = linalg.solve_banded((l, u), ab, b)
    print(ans)


# In[ ]:




