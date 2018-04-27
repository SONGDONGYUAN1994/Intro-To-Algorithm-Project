m = 1000
x = np.loadtxt("D:\MS\Master Course\BST234\Project\simulated_genos", delimiter=" ", dtype="float32")
x_sparse = sparse.csr_matrix(x)
xxt_sparse = x_sparse @ x_sparse.transpose()
q = np.empty((m, 1))

for i in range(m):
    y_cc = np.zeros((20000, 1)) - 0.5
    y_cc[np.random.choice(20000, size = 10000, replace = False)] = 0.5
    q[i,0] = y_cc.T @ xxt_sparse @ y_cc
    #q00 = y_cc.T @ xxt_sparse
    #q11 = (y_cc.T * q00).sum(axis=1)