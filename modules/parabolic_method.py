#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 22:52:05 2018

@author: ricktjwong
"""

import numpy as np


def lagrange_polynomial(v, x, y, o):
    """
    Calculates the point f(v) for a nth degree polynomial when given the x
    coordinate v and the x and y array of points
    """
    total_sum = 0
    for i in range(o + 1):
        product = 1
        for j in range(o + 1):
            if i != j: product *= (v - x[j]) / (x[i] - x[j])
        product *= y[i]
        total_sum += product
    return total_sum


def test_p2(v, x, y):
    A = ((v - x[1]) * (v - x[2])) / ((x[0] - x[1]) * (x[0] - x[2])) * y[0]
    B = ((v - x[0]) * (v - x[2])) / ((x[1] - x[0]) * (x[1] - x[2])) * y[1]
    C = ((v - x[0]) * (v - x[1])) / ((x[2] - x[0]) * (x[2] - x[1])) * y[2]
    return A + B + C


def p2_minima(x, y):
    num = ((x[2] * x[2] - x[1] * x[1]) * y[0] + \
           (x[0] * x[0] - x[2] * x[2]) * y[1] + \
           (x[1] * x[1] - x[0] * x[0]) * y[2])
    denom = (x[2] - x[1]) * y[0] + \
            (x[0] - x[2]) * y[1] + \
            (x[1] - x[0]) * y[2]
    minima = 0.5 * num / denom
    return minima


def objective(x):
    return x ** 3 - 2 * x ** 2

min_x = 4 / 3

x = np.array([1., 1.5, 2.])
y = objective(x).copy()

n = 0
while(n < 100):
    new_min = p2_minima(x, y)
    x = np.append(x, new_min)
    x.sort()
    x = x[:-1].copy()
    y = objective(x).copy()
    n += 1

print(n)
print(new_min)
     