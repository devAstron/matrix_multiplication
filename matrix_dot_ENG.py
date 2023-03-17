-- coding: utf-8 --
"""
Created on Fri Mar 17 20:05:40 2023

@author: Bahodir

Hello, this program performs matrix multiplication on two matrices of size NxM and MxN.
Steps:
1. Write a function called for_matrix1 that accepts the values of n and m for an NxM matrix from the user,
prompts the user to enter the elements of the NxM matrix,
and returns a numpy array called matrix1;
2. Write a function called for_matrix2 that accepts the values of m and n for an MxN matrix from the user,
prompts the user to enter the elements of the MxN matrix,
and returns a numpy array called matrix2;
3. Write a function called for_multiply that takes two matrices as input,
performs matrix multiplication on the two matrices,
and returns the resulting matrix called result.
We need the numpy library to write this program, of course!!!
Let's get started!😍😍😍
"""

import numpy as np

def for_matrix1():
n = int(input('Enter the number of rows of the first matrix: '))
m = int(input('Great, now enter the number of columns of the first matrix: '))
matrix1 = np.zeros((n, m))
for i in range(n):
for j in range(m):
matrix1[i][j] = float(input(f"Enter the ({i+1}, {j+1}) element of the matrix: "))
return matrix1

def for_matrix2():
try:
m = int(input('Now onto the second matrix, enter the number of rows of the second matrix: '))
n = int(input('Enter the number of columns of the matrix: '))
matrix2 = np.zeros((m, n))
for i in range(m):
for j in range(n):
matrix2[i][j] = float(input(f"Enter the ({i+1}, {j+1}) element of the matrix: "))
return matrix2
except:
print('Sorry, you made a mistake when entering the number of rows and columns of the matrix.')

def for_multiply(arr1, arr2):
if arr1.shape[1] != arr2.shape[0]:
print('These two matrices cannot be multiplied because the number of columns in the first matrix is not equal to the number of rows in the second matrix!')
return
else:
result = np.dot(arr1, arr2)
return result

matrix1 = for_matrix1()
print(f"The first matrix entered: \n{matrix1}")
matrix2 = for_matrix2()
print(f"The second matrix entered: \n{matrix2}")
result = for_multiply(matrix1, matrix2)
print('The result of multiplying the two matrices: \n', result)