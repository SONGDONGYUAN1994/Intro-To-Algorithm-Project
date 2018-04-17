import numpy as np
import time
from scipy import sparse
import random
import matplotlib.pyplot as plt


def prep_data():
    x = np.loadtxt("simulated_genos", delimiter=" ", dtype="float32")
    y = np.array([[1] * 10000 + [0] * 10000], dtype="float32")
    y_c = y - 0.5
    return x, y_c

x, y_c = prep_data()


X = x
print(X.shape)
n = X.shape[0]
p = X.shape[1]
print("Dimension of X", n, p)


start_time = time.clock()

V = np.identity(n)
print("Matrix V", V)

x1 = np.ones(shape=(n, 1))
X_tu = np.concatenate((x1, X), axis=1)
print("Design Matrix", X_tu.shape)


P_0 = V - (V @ X_tu @ np.linalg.inv(X_tu.T @ V @ X_tu) @ X_tu.T @ V)

print("Dimension of P_0", P_0.shape)
print("P_0", P_0)