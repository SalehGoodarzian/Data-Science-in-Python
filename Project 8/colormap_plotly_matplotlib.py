import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_excel('data.xlsx', sheet_name=0)
df.set_index('x', inplace=True)
x = df.index.tolist()
n = df.shape[1]

# print('\n==== Example 1: Sequential colormap in matplotlib ====')
# cmap = plt.colormaps['plasma']             # https://matplotlib.org/stable/users/explain/colors/colormaps.html
# cc = cmap(np.linspace(0, 1, n))
# for i in range(n):
#     y = df.iloc[:, i].tolist()
#     plt.plot(x, y, linewidth=2.5, color=cc[i])
# plt.show()

# print('\n==== Example 2: Qualitative colormap in matplotlib ====')
# cc = plt.colormaps['tab10'].colors
# for i in range(n):
#     y = df.iloc[:, i].tolist()
#     plt.plot(x, y, linewidth=2.5, color=cc[i])
# plt.show()

# print('\n==== Example 3: Sequential colormap in plotly (line plot) ====')
# cc = px.colors.sample_colorscale('Viridis', np.linspace(0, 1, n))
# fig = go.Figure()
# for i in range(n):
#     y = df.iloc[:, i].tolist()
#     fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line={'color': cc[i]}))
# fig.show()

# print('\n==== Example 4: Sequential colormap in plotly (bar chart) ===========')
# cc = px.colors.sample_colorscale('Viridis', np.linspace(0, 1, n))
# fig = go.Figure()
# for i in range(n):
#     y = df.iloc[:, i].tolist()
#     fig.add_bar(x=x, y=y, marker_color=cc[i])
# fig.show()

# print('\n==== Example 5: Qualitative colormap in plotly (line plot) ====')
# cc = px.colors.qualitative.Alphabet
# fig = go.Figure()
# for i in range(n):
#     y = df.iloc[:, i].tolist()
#     fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line={'color': cc[i]}))
# fig.show()

# print('\n==== Example 6: Qualitative colormap in plotly (bar chart) ====')
# cc = px.colors.qualitative.Alphabet
# fig = go.Figure()
# for i in range(n):
#     y = df.iloc[:, i].tolist()
#     fig.add_bar(x=x, y=y, marker_color=cc[i])
# fig.show()
