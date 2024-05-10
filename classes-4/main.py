import numpy as np

t = np.array([1, 2, 3])
t1 = np.zeros(10)
t2 = np.ones((3, 5))
print(t1)
print(t2)

# computational mesh
l = np.linspace(0, 1, 5)
print(l)
l0 = np.linspace(0, 1, 11)
print(l0)

l1 = np.linspace(0, 1, 6)  # <start,stop>
l2 = np.arange(0, 1, 0.2)  # <start,stop)
print(l1)
print(l2)

# ------------

lp = [1, 2, 3, 4]
print(lp * 3)
lp1 = np.arange(1, 5, 1)
print(lp1 * 3)

# ------------

x = np.array([i for i in range(10)])
print(np.sin(x))
# np.sin() np.pi() np.exp()
print(np.logical_and(x > 2, x < 5))

# simple chart
import matplotlib.pyplot as plt

x = [i for i in range(1, 11)]
y = list(map(lambda i: i ** 2, x))
# print(plt.plot(x,y,marker="o",linestyle="dashdot"))
# plt.show()

# print(plt.scatter(x,y,marker="o", color="black"))
# plt.show()

import math

z1 = [i / 100 for i in range(0, 628)]
z2 = list(map(lambda i: math.sin(i), z1))
plt.scatter(z1, z2)
plt.show()
