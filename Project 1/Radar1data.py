import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel('data.xlsx', sheet_name=0)
print(df.head(10))

items = ['Cars', 'Trucks', 'Trains']

# fig = go.Figure()
# fig.add_trace(go.Scatterpolar(r=df.iloc[:, 1], theta=df.iloc[:, 0], name=items[0]))

fig = go.Figure()
for i in range(3):
    fig.add_trace(go.Scatterpolar(r=df.iloc[:, i + 1], theta=df.iloc[:, 0], name=items[i]))

fig.update_traces(fill='toself')
fig.update_traces(showlegend=True)
fig.update_layout(legend={'font_size': 15, 'font_weight': 'bold', 'x': 0.8, 'y': 0.96})
fig.update_layout(title={'text': 'Asia', 'font_size': 30, 'font_weight': 'bold', 'x': 0.5, 'y': 0.96})
fig.update_polars(gridshape='linear', angularaxis_tickfont={'size': 14, 'weight': 'bold'})
fig.update_polars(radialaxis_range=[0, 1], radialaxis_dtick=0.2, radialaxis_showticklabels=True)
fig.update_layout(template=None)

fig.show()

