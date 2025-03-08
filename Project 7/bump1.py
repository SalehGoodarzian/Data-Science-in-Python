import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data.xlsx', sheet_name=0)
df.set_index('Items', inplace=True)
df.sort_values('Air', inplace=True)     # or df.columns.tolist()[0]
print(df.head())

dfnew = pd.DataFrame()
for col in df.columns.tolist():
    dfnew[col] = df[col].rank(ascending=True)
print("\n===== Ranked sorted DataFrame =======")
print(dfnew)

x = [1, 2, 3]
for i in range(dfnew.shape[0]):
    y = dfnew.values.tolist()[i]
    size = [5 * n for n in df.values.tolist()[i]]
    plt.scatter(x, y, marker='o', s=size)
    plt.plot(x, y)

plt.grid()
plt.gca().invert_yaxis()
plt.xlabel('Environmental parameters', fontsize=14, fontweight='bold', labelpad=10)
plt.xticks(x, df.columns.tolist(), fontsize=12)
plt.ylabel('Items', fontsize=14, fontweight='bold', labelpad=10)
plt.yticks([1, 2, 3, 4, 5], df.index.tolist(), fontsize=12)
plt.show()