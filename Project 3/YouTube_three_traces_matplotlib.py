import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

continents = ['Aisa', 'Europe', 'America', 'Africa', 'Australia']
a = 0
df = pd.read_excel('data.xlsx', sheet_name=a)
items = ['Cars', 'Trucks', 'Trains']

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, dpi=150)

parameters = df.iloc[:, 0].tolist()                                   # generating a list of labels for different parameters
theta = np.linspace(0, 360, len(parameters))                # generating a list for the angular location of each parameter

for b in range(len(items)):
    r = df.iloc[:, b + 1].tolist()                                    # generating a list for the value of each parameter
    ax.plot(np.deg2rad(theta), r, marker='o', markersize=5, label=items[b])
    ax.fill(np.deg2rad(theta), r, alpha=1)

ax.set_thetagrids(theta, parameters, font={'size': 9, 'weight': 'bold'})      # showing labels for angles
ax.set_rmax(1)                                                                # setting the radius of the circle
# ax.set_rgrids([0.25, 0.50, 0.75, 1], [0.25, 0.50, 0.75, 1], fontsize=6, angle=20)
ax.set_rgrids([0.25, 0.50, 0.75, 1], ['Fail', 'Pass', 'Good', 'Excellent'], fontsize=6, angle=20)

fig.suptitle(continents[a], font={'size': 18, 'weight': 'bold'}, y=0.99)      # setting title properties
fig.legend(prop={'size': 12, 'weight': 'bold'}, loc=(0.75, 0.75))             # setting legend properties
plt.show()