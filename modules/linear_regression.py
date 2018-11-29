#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 23:39:29 2018

@author: ricktjwong
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/headbrain.csv")
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values

"""
SE = sum ([x_i - f(x_i)]^2) ----- Eq. (1)
f(x) = b0 + b1 * x ----- Eq. (2)

We can get the minimum squared error by substituting Eq. (2) into Eq. (1): 
    
    SE = sum ([x_i - (b0 + b1 * x_i)]^2) ----- Eq. (3)
    
By taking the partial derivative of SE w.r.t. b0 and partial derivative of SE
w.r.t. b1, we can set these to zero and solve to get equations for b0 and b1

b1 = sum [(x_i - mu_x) * (y_i - mu_y)] / sum [(x_i - mu_x)^2]
b0 = mu_y - (b1 * mu_x)
"""

mu_x = sum(X) / len(X)
mu_y = sum(Y) / len(Y)

b1 = sum([(i - mu_x) * (j - mu_y) for i,j in zip(X, Y)]) / \
     sum([(i - mu_x) ** 2 for i in X])
b0 = mu_y - (b1 * mu_x)


def f(x):
    return b0 + b1 * x

plt.scatter(X, Y, c='b', s=1, label='Data')
plt.plot(X, f(X), c='red', label='f(x) = b0 + b1 * x')
plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()

var = sum([1/len(Y) * (f(X[i]) - Y[i]) ** 2 for i in range(len(X))])
rmse = var ** 0.5

ss_t = sum([(Y[i] - mu_y) ** 2 for i in range(len(X))])
ss_r = sum([(f(X[i]) - Y[i]) ** 2 for i in range(len(X))])
r2 = 1 - ss_r/ss_t
print(r2)
