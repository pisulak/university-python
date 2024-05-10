import random as rand
import numpy as np
import matplotlib.pyplot as plt

def f1(x, y):
    return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6

def f2(x, y):
    return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

def f3(x, y):
    return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6

def f4(x, y):
    return 0, 0.16 * y

functions = [f1, f2, f3, f4]
weights = [0.85, 0.07, 0.07, 0.01]

x = 0
y = 0
for i in range(10000):
    choice = np.random.choice(range(4), p=weights)
    x, y = functions[choice](x, y)
    plt.scatter(x, y, color='green', marker='.', linestyle='', s=0.2)
plt.show()
