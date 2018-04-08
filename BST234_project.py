import numpy as np
import time


X = np.loadtxt("simulated_genos", delimiter=" ", dtype='int32')  # dtype?

print(X.shape)

Y = np.array([[1] * 10000 + [0] * 10000])
print(Y.shape)

Y_c = Y - 0.5

print(Y_c.view())

start_CPU = time.clock()
XXt = np.dot(X, X.T)
end_CPU = time.clock()

print((XXt.shape, (end_CPU - start_CPU)))

start_CPU = time.clock()
Q = (Y_c.dot(XXt) * Y_c).sum(axis=1)  # Calculate the quadratic form has many ways. This might not be the fastest.
end_CPU = time.clock()
print((Q, (end_CPU - start_CPU)))

start_CPU = time.clock()
Y_c1 = np.random.shuffle(Y_c)
end_CPU = time.clock()
print(end_CPU-start_CPU)
