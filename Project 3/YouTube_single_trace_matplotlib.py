import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

continents = ['Aisa', 'Europe', 'America', 'Africa', 'Australia']
a = 0
df = pd.read_excel('data.xlsx', sheet_name=a)

items = ['Cars', 'Trucks', 'Trains']
b = 0
parameters = df.iloc[:, 0].tolist()                         # generating a list of labels for different parameters
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, dpi=150)

r = df.iloc[:, b + 1].tolist()                              # generating a list for the values of different parameters
theta = np.linspace(0, 360, len(parameters))       # generating a list for the angular location of different parameters
ax.plot(np.deg2rad(theta), r, marker='o', markersize=5, color='blue', label=items[b])
ax.fill(np.deg2rad(theta), r, color='blue', alpha=1)

ax.set_thetagrids(theta, parameters, font={'size': 9, 'weight': 'bold'})    # showing labels at prescribed angles
ax.set_rmax(1)                                                              # setting the radius of the circle
# ax.set_rgrids([0.25, 0.50, 0.75, 1], [0.25, 0.50, 0.75, 1], fontsize=6, angle=20)
ax.set_rgrids([0.25, 0.50, 0.75, 1], ['Fail', 'Pass', 'Good', 'Excellent'], fontsize=6, angle=15)

fig.suptitle(continents[a], font={'size': 18, 'weight': 'bold'}, y=0.99)     # setting title properties
fig.legend(prop={'size': 12, 'weight': 'bold'}, loc=(0.75, 0.80))            # setting legend properties
plt.show()