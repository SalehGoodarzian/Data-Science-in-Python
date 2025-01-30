import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('data_different_scale.xlsx', sheet_name=0)
items = ['Manchester city', 'Everton']
parameters = df.iloc[:, 0].tolist()
theta = np.linspace(0, 360, len(parameters))

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, dpi=150)

for b in range(len(items)):
    nr = df.iloc[:, b + 4].tolist()
    ax.plot(np.deg2rad(theta), nr, marker='o', markersize=5, label=items[b])
    ax.fill(np.deg2rad(theta), nr, alpha=0.5)
ax.set_rmax(1)
loc = [0.25, 0.50, 0.75, 1]
ax.set_rgrids(loc, [])
ax.set_thetagrids(theta, parameters, fontsize=7)
ax.set_title('Multiple scales on multiple axes', font={'size': 13, 'weight': 'bold'}, y=1.07)
ax.legend(loc=(0.95, 0.95), prop={'size': 8, 'weight': 'bold'})

decimal = df.iloc[:, 8].tolist()
for i in range(len(theta)):
    actual = np.linspace(0, df.iloc[i, 3], len(loc) + 1)[1:]
    for j in range(len(loc)):
        if decimal[i] == 0:
            ax.text(np.deg2rad(theta[i]), loc[j], round(actual[j]), fontsize=5)
        else:
            ax.text(np.deg2rad(theta[i]), loc[j], round(actual[j], decimal[i]), fontsize=5)

plt.show()