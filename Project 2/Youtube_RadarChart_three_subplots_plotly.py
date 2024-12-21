import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

continents = ['Asia', 'Europe', 'America', 'Africa', 'Australia']
a = 0
df = pd.read_excel('data.xlsx', sheet_name=a)

items = ('Cars', 'Trucks', 'Trains')
fig = make_subplots(rows=1, cols=3,
                    specs=[[{'type': 'polar'}, {'type': 'polar'}, {'type': 'polar'}]],
                    subplot_titles=items, horizontal_spacing=0.1)

fig.add_trace(go.Scatterpolar(r=df.iloc[:, 1], theta=df.iloc[:, 0], line={'color': 'orange'}), row=1, col=1)
fig.add_trace(go.Scatterpolar(r=df.iloc[:, 2], theta=df.iloc[:, 0], line={'color': 'blue'}), row=1, col=2)
fig.add_trace(go.Scatterpolar(r=df.iloc[:, 3], theta=df.iloc[:, 0], line={'color': 'green'}), row=1, col=3)

fig.update_traces(fill='toself')
fig.update_traces(showlegend=False)
fig.update_annotations(font_size=19, font_weight='bold', y=0.87)
fig.update_layout(title={'text': continents[a], 'font_size': 28, 'font_weight': 'bold', 'x': 0.5, 'y': 0.88})
fig.update_polars(gridshape='linear', angularaxis={'tickfont_size': 13, 'tickfont_weight': 'bold'})
fig.update_polars(radialaxis={'range': [0, 1], 'dtick': 0.2, 'angle': 80, 'tickangle': 80})
# fig.update_polars(radialaxis={'range': [0, 1], 'tickvals': [0.2, 0.4, 0.6, 0.8, 1],
#                               'ticktext': ['Very low', 'Low', 'Normal', 'High', 'Very high'],
#                               'angle': 80, 'tickangle': 80, 'tickfont_size': 10})
fig.update_layout(template=None)
fig.show()
