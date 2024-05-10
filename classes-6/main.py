import matplotlib.pyplot as plt
import time

c = -0.1 + 0.65j

x = []
y = []

colors = []


def julia_set(z, c):
    for i in range(300):
        z = z ** 2 + c
        if abs(z) > 2:
            return i
    return 300


start_t = time.time()
d = 400
for i in range(d):
    for j in range(d):
        xi = -1.5 + 3 / d * i
        yi = -1.5 + 3 / d * j
        x.append(xi)
        y.append(yi)
        colors.append(julia_set(xi + yi * 1j, c))

print(time.time() - start_t)
# plt.figure(figsize=(10,10))
# plt.scatter(x,y,c=colors,s=0.1)
# plt.axis('square')
# plt.show()

# --------------------------------------------

import matplotlib as plt
import numpy as np

c = -0.1 + 0.65j
d = 400

X, Y = np.meshgrid(np.linspace(-1.5, 1.5, d), np.linspace(-1.5, 1.5, d))


def julia_set(z, c):
    for i in range(300):
        z = z ** 2 + c
        if np.abs(z) > 2:
            return np.int(i)
        return np.int(300)


colors = julia_set(X + Y * 1j, c)
plt.figure(figsize=(10, 10))
plt.scatter(X, Y, c=colors, s=0.4)
plt.axis('square')
plt.show()
