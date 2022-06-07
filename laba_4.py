#!/usr/bin/env python
# coding: utf-8

# In[2]:


from math import pi, atan, cos, sin, sqrt

eps = 0.01

matrix = [[8,-3,9],
         [-3,8,-2],
         [9,-2,8]]

def find_max(array):
    n = len(array)
    i_r, j_r = 0, 0
    max = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(array[i][j]) > max:
                max = abs(array[i][j])
                i_r = i
                j_r = j
    return i_r, j_r


def transpose(array):
    n = len(array)
    m = len(array[0])
    result = [[0 for j in range(n)] for i in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][i] = array[i][j]
    return result


def matrix_product(array1, array2):
    n1 = len(array1)
    m1 = len(array1[0])
    n2 = len(array2)
    m2 = len(array2[0])
    if m1 != n2:
        print('Matrix product error')
        exit()
    result = [[0 for _ in range(m2)] for _ in range(n1)]
    for i in range(n1):
        for k in range(m2):
            for j in range(m1):
                result[i][k] += array1[i][j] * array2[j][k]
    return result


def spin_method(array):
    n = len(array)
    new_array = array.copy()
    eigenvectors = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
    while True:
        i_max, j_max = find_max(new_array)
        if new_array[i_max][i_max] == new_array[j_max][j_max]:
            phi = pi / 4
        else:
            phi = 0.5 * atan((2 * new_array[i_max][j_max]) / (new_array[i_max][i_max] - new_array[j_max][j_max]))

        U = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
        U[i_max][i_max] = cos(phi)
        U[j_max][j_max] = cos(phi)
        U[i_max][j_max] = -sin(phi)
        U[j_max][i_max] = sin(phi)

        eigenvectors = matrix_product(eigenvectors, U)

        UT = transpose(U)
        new_array = matrix_product(matrix_product(UT, new_array), U)
        eps_k = 0
        for i in range(n):
            for j in range(i):
                eps_k += new_array[i][j] ** 2
        eps_k = sqrt(eps_k)
        if eps_k < eps:
            break

    eigenvalues = [round(new_array[i][i], 2) for i in range(n)]
    eigenvectors = [[round(eigenvectors[i][j], 4) for j in range(n)] for i in range(n)]

    return eigenvalues, eigenvectors

print(f'epsilon = {eps}\n')
eigenvalues, eigenvectors = spin_method(matrix)
print('eigenvalues:')
print(eigenvalues)
print('eigenvectors')
for i in range(len(eigenvectors)):
    print(f'h{i} = ', end='')
    for j in range(len(eigenvectors)):
        print(f'{eigenvectors[j][i]:.2f}', end=' ')
    print()


# In[ ]:




