import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('databar.xlsx', sheet_name=0)
df.set_index('Time', inplace=True)

cols = df.columns.tolist()
x = [1, 3, 4, 6, 7]
b = [0] * len(x)
for i in range(df.shape[1]):
    y = df.iloc[:, i].tolist()
    plt.bar(x, y, width=0.75, bottom=b, label=cols[i])
    b = [b[i] + y[i] for i in range(len(b))]
    for m, n in enumerate(x):
        plt.text(n, b[m], b[m], ha='center', fontsize=9)

plt.legend(title='Items', title_fontproperties={'size': 14, 'weight': 'bold'},
           loc='upper left', reverse=True, fontsize=12, frameon=True)
plt.grid(True, which='major', linestyle='--', linewidth=0.3, color='0.5')

plt.ylabel('Greenhouse gas CO$_2$ emissions', fontsize=16, fontweight='bold', labelpad=10)
plt.ylim([0, 50])
plt.yticks(np.arange(0, 51, 10), fontsize=14, rotation=0)

plt.xlabel('Sources of CO$_2$', fontsize=16, fontweight='bold', labelpad=10)
plt.xticks(x, df.index.tolist(), fontsize=14, rotation=0)

plt.show()