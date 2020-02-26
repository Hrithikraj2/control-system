# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:27:28 2020

@author: Hrithik
"""
# Python program to demonstrate
# indexing in numpy array
def Routh_Hurwitz(coef):
    l = len(coef)
    even = list(coef[0::2][:])
    odd = list(coef[1::2][:])
    for i in range(3):
        if len(even) <= 3:
            even.append(0)
        if len(odd) <= 3:
            odd.append(0)
    curr = odd[:]
    prev = even[:]
    matrix = []
    matrix.append(prev)
    matrix.append(curr)
    for i in range(l-2):
        temp = []
        for j in range(len(curr)-1):
            if abs(curr[0]) <= 1e-3:
                a = 0.01
            else:
                a = curr[0]
            temp.append(-np.linalg.det(np.array([[prev[0] ,prev[j+1]],[a, curr[j+1]]]))/a)
        matrix.append(temp)
        prev = curr[:]
        curr = temp[:]
    for i in matrix:
        print(i)