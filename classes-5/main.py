import numpy as np
import matplotlib.pyplot as plt

# X=np.linspace(0, 1, 51)
# for a in np.linspace(0.25, 2, 8):
#     plt.plot(X,X**a, color='black')
# plt.legend()
# plt.show()

# T=np.linspace(0,2*np.pi,1000)        #circle
# plt.scatter(np.sin(T), np.cos(T))
# plt.show()

X = np.linspace(-3, 3, 500)
Y = 1 / (X ** 2 - 1)
Y[abs(Y) > 10] = np.NaN
plt.figure(figsize=(15, 5))
plt.plot(X, Y)
plt.plot([-1, -1], [-10, 10], '--')
plt.show()
