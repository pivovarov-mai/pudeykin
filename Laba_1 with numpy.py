#!/usr/bin/env python
# coding: utf-8

# ## with NumPy

# In[26]:


from numpy import array, zeros
a=array([[-5,-1,-3,-1],
         [-2,0,8,-4],
         [-7,-2,2,-2],
         [2,-4,-4,4]],float )
b=array([18,-12,6,-12],float)
n=len(b)
x=zeros(n,float)

for k in range(n-1):
    for i in range(k+1,n):
        if a[i,k]==0:continue
        factor=a[k,k]/a[i,k]
        for j in range(k,n):
            a[i,j]=a[k,j]-a[i,j]*factor
        b[i]=b[k]-b[i]*factor
x[n-1]=b[n-1]/a[n-1,n-1]
for i in range(n-2,-1,-1):
    sum_ax=0
    for j in range(i+1,n):
        sum_ax += a[i,j]*x[j]
    x[i]=(b[i]-sum_ax)/a[i,i]
print('result:',x)    


# In[ ]:




