import numpy as np
import time


def prep_data():
    x = np.loadtxt("simulated_genos", delimiter=" ", dtype="float32")
    y = np.array([[1] * 10000 + [0] * 10000], dtype="float32")
    y_c = y - 0.5
    return x, y_c


def main():
    x, y_c = prep_data()
    start_time = time.clock()
    xxt = np.dot(x, x.T)
    end_time = time.clock()
    print('xxt computation time: ', end_time - start_time)
    start_time = time.clock()
    ry_matrix = RYSparseMatrix(xxt)
    end_time = time.clock()
    print('ry matrix load time: ', end_time - start_time)
    start_time = time.clock()
    # q = (y_c.dot(xxt) * y_c).sum(axis=1)
    # q0 = y_c.dot(xxt)
    q0 = ry_matrix.multiply_y_c(y_c)
    q1 = (q0 * y_c).sum(axis=1)
    end_time = time.clock()
    print('ry q computation time: ', end_time - start_time)
    start_time = time.clock()
    # q = (y_c.dot(xxt) * y_c).sum(axis=1)
    q0 = y_c.dot(xxt)
    q2 = (q0 * y_c).sum(axis=1)
    end_time = time.clock()
    print('original q computation time: ', end_time - start_time)
    if q1 == q2:
        print('computation results are the same')
    else:
        print('computation results are different')
    print('q1: ', q1)
    print('q2: ', q2)


class RYSparseMatrix(object):
    def __init__(self, matrix):
        matrix = matrix.T
        h, w = matrix.shape
        result = []
        for i in range(h):
            temp = []
            matrix_line = matrix[i].tolist()
            for index, value in enumerate(matrix_line):
                if value > 0.5:
                    temp.append(index)
            result.append(temp)
        self.matrix = result

    def multiply_y_c(self, y_c):
        y_c_p = y_c.tolist()
        result = [[0]*20000]
        for i, line in enumerate(self.matrix):
            for index in line:
                result[0][i] += y_c_p[0][index]
        return np.array(result, dtype="float32")


if __name__ == '__main__':
    main()