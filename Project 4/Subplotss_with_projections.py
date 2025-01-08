import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 3, subplot_kw={'projection': 'polar'},
                       gridspec_kw={'wspace': 0.5}, dpi=140)

a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'A']
car1 = [0.14, 0.22, 0.60, 0.18, 0.03, 0.65, 0.70, 1.00, 1.00, 0.14]
car2 = [0.56, 0.68, 0.04, 0.05, 0.35, 0.87, 0.10, 0.20, 0.30, 0.56]
car3 = [0.06, 0.10, 0.85, 0.65, 0.38, 0.17, 0.40, 0.20, 0.10, 0.06]
theta = np.linspace(0, 360, len(a))

ax[0].plot(np.deg2rad(theta), car1)
ax[1].plot(np.deg2rad(theta), car2)
ax[2].plot(np.deg2rad(theta), car3)
plt.show()