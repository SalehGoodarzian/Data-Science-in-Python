import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 3, 4, 5, 6, 7, 8]

fig = plt.figure()

ax1 = fig.add_subplot(131)
ax1.scatter(x, y)

ax2 = fig.add_subplot(132)
ax2.plot(x, y)

ax3 = fig.add_subplot(133, projection='polar')
r = [0.8, 0.9, 0.7, 0.25, 0.4, 0.8, 0.2, 0.1, 0.8]
theta = np.linspace(0, 360, len(r))
ax3.plot(np.deg2rad(theta), r)

plt.show()