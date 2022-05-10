#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
a = np.array([[21, -6, -9,-4], [-6, 20, -4,2], [-2, -7, -20,3], [4, 9, 6,24]])
b = np.array([127,-144,236,-5])
x = np.array([0, 0, 0,0])     # Начальное значение итерации
g = 1e-6              # Точность
def Seidel(a, b, x, g):  
    x = x.astype(float)    # Установиk точность x, чтобы при вычислении x можно было отображать несколько десятичных знаков
    m, n = a.shape
    iterations = 0            # Итерации
    if (m < n):
        print('Есть пространство для решения')    # Убедимся, что количество уравнений больше, чем количество неизвестных
    else:
        while True:
            for i in range(n):
                s = 0
                ans = x.copy()        # Записываем ответ последней итерации
                for j in range(n):
                    if i != j:
                        s += x[j] * a[i][j]
                x[i] = (b[i] - s) / a[i][i]
                iterations += 1                                 
            r = max(abs(x - ans))              # Отличие от последнего модуля ответа

            if r < g:                          # Точность соответствует требованиям
                break

            elif iterations > 1000:          # Если итерация превышает 1000 Раз
                break
                print('1000 итераций все равно не сходятся')

    print(iterations)
    print(x)


if __name__ == '__main__':   
    Seidel(a, b, x, g)


# In[ ]:




