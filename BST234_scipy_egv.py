import numpy as np
import time
import scipy as sp
from scipy import sparse
import random
import matplotlib.pyplot as plt
import scipy.sparse.linalg as lg

def prep_data():
    x = np.loadtxt("simulated_genos", delimiter=" ", dtype="float32")
    y = np.array([[1] * 10000 + [0] * 10000], dtype="float32")
    y_c = y - 0.5
    return x, y, y_c

x, y, y_c = prep_data()

x, y, y_c = prep_data()

n = 20000
X = x[:,:]
print("X shape:", X.shape)
print("Rank of X:", np.linalg.matrix_rank(X))
print ("Number of 1:",np.sum(x))
n = X.shape[0]
p = X.shape[1]
print (n,p)

X_sparse = sparse.csr_matrix(X)
print("Type of X_sparse:", type(X_sparse))

np_SVD_result = sp.linalg.svdvals(X[:n,:])
print("X SV:", np_SVD_result, len(np_SVD_result))


sp_SVD_result = lg.svds(X_sparse, k = 49)
print("X_sparse SV:", sp_SVD_result[1])

print(sorted((sp_SVD_result[1])**2, reverse=True))

XX_t = X @ X.T

print("Rank of XX_t:", np.rank(XX_t))

XX_t_sparse = X_sparse @ X_sparse.T
#sp.rank(XX_t_sparse)
ev_sparse = lg.eigs(XX_t_sparse, k=50)
ev_sparse = np.real(ev_sparse[0])
print(sorted(ev_sparse, reverse=True))

sum(ev_sparse / 4)
