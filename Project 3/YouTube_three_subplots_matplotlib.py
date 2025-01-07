import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

continents = ['Aisa', 'Europe', 'America', 'Africa', 'Australia']
a = 0
df = pd.read_excel('data.xlsx', sheet_name=a)
items = ['Cars', 'Trucks', 'Trains']

fig, ax = plt.subplots(1, 3, subplot_kw={'projection': 'polar'}, gridspec_kw={'wspace': 0.5}, dpi=150)

parameters = df.iloc[:, 0].tolist()                            # generating a list of labels for different parameters
theta = np.linspace(0, 360, len(parameters))          # generating a list for the angular location of each parameter

for b in range(len(items)):
    r = df.iloc[:, b + 1].tolist()                             # generating a list for the value of each parameter
    ax[b].plot(np.deg2rad(theta), r, marker='o', markersize=5, label=items[b])
    ax[b].fill(np.deg2rad(theta), r, alpha=0.5)
    ax[b].set_title(items[b], font={'size': 12, 'weight': 'bold'})

    ax[b].set_thetagrids(theta, parameters, font={'size': 7, 'weight': 'bold'})    # showing labels for angles
    ax[b].set_rmax(1)                                                              # setting the radius of the circle
    # ax[b].set_rgrids([0.25, 0.50, 0.75, 1], [0.25, 0.50, 0.75, 1], fontsize=6, angle=20)
    ax[b].set_rgrids([0.25, 0.50, 0.75, 1], ['Fail', 'Pass', 'Good', 'Excellent'], fontsize=5, angle=20)

fig.suptitle(continents[a], y=0.85, font={'size': 18, 'weight': 'bold'})
plt.show()