#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.linalg import solve
a=([[-5,-1,-3,-1],
         [-2,0,8,-4],
         [-7,-2,2,-2],
         [2,-4,-4,4]])
b=([18,-12,6,-12])
x=solve(a,b)
print(x)


# In[ ]:




