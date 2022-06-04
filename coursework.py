#!/usr/bin/env python
# coding: utf-8

# ## Метод ньютона
# 

# In[23]:


import math
import matplotlib.pyplot as plt
import pylab
eps=1e-6
iters=0
def f(x) :
    return x*math.exp(x)+x**2-1
def derrirative(x) :              #производная
    return math.exp(x)+x*math.exp(x)+2*x
 
def Newtons(a,b):
    xn = (a+b)/2
    xn1 = xn - f(xn) / derrirative(xn)
    iters=1
    while abs(xn1-xn) > eps:
        xn = xn1
        xn1 = xn - f(xn) / derrirative(xn)
        if abs(xn1 - xn)<= eps:
            return xn1, iters
        iters += 1


print(Newtons(0.2, 0.5))

x0=-1.3
list_x=[(x0+0.1*i) for i in range (0,21,1)]
y = [f(x) for x in list_x]
sp = plt.subplot(111)
pylab.plot(list_x, y)
sp.spines['bottom'].set_position('center')


# ## Метод простой итерации

# In[10]:


import math
import matplotlib.pyplot as plt
import pylab
import numpy as np
eps=1e-6
iters=0
def f(x) :
    return  1/(math.exp(x)+x)

def Iterative_Method(a,b):
    xn = (a+b)/2
    xn1 = f(xn)
    iters=1
    while (abs(xn1 - xn) > eps):
        iters += 1
        xn = xn1
        xn1 = f(xn)
    print ("\nКоличество итераций:", iters)
    return xn1

print(Iterative_Method(0.2,0.5))


# ##### В разных же методах, несмотря на большую разницу количества итераций, корень уравнения остаётся одним и тем же. Если менять точность вычислений(eps), то корень уравнения не сильно изменяется. Тогда можно сказать, что погрешность выислений от итераций мала. 

# In[ ]:




