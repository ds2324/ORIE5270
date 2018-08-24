from scipy.optimize import minimize, rosen

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    trials = 1000
    n = 3
    x0_matrix = np.random.rand(trials,n)
    fun_value = []

    for i in range(trials):
        x0 = x0_matrix[i, :]
        res = minimize(rosen, x0, method='BFGS')
        fun_value.append(res.fun)

    print("The average of the minimized value is %f" % np.mean(fun_value))
    plt.hist(fun_value, bins = 'auto')
    plt.title("Histogram with 'auto' bins")
    plt.show()

