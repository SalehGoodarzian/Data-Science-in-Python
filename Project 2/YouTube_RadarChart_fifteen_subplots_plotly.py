import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

items = ('Asia (Cars)', 'Asia (Trucks)', 'Asia (Trains)',
      'Europe (Cars)', 'Europe (Trucks)', 'Europe (Trains)',
      'America (Cars)', 'America (Trucks)', 'America (Trains)',
      'Africa (Cars)', 'Africa (Trucks)', 'Africa (Trains)',
      'Australia (Cars)', 'Australia (Trucks)', 'Australia (Trains)')

rr = 5
cc = 3
sp = rr * [cc * [{'type': 'polar'}]]
fig = make_subplots(rows=rr, cols=cc, specs=sp, subplot_titles=items)

for ii in range(rr):
    df = pd.read_excel('data.xlsx', sheet_name=ii)
    fig.add_traces([go.Scatterpolar(r=df.iloc[:, 1], theta=df.iloc[:, 0], line={'color': 'orange'})], rows=ii + 1, cols=1)
    fig.add_traces([go.Scatterpolar(r=df.iloc[:, 2], theta=df.iloc[:, 0], line={'color': 'blue'})], rows=ii + 1, cols=2)
    fig.add_traces([go.Scatterpolar(r=df.iloc[:, 3], theta=df.iloc[:, 0], line={'color': 'green'})], rows=ii + 1, cols=3)

fig.update_traces(fill='toself')
fig.update_traces(showlegend=False)
fig.update_annotations(font_size=14, font_weight='bold', yshift=15)
fig.update_layout(title={'text': 'Effect of items on parameters', 'font_size': 24, 'font_weight': 'bold', 'x': 0.5, 'y': 0.97})
fig.update_polars(gridshape='linear', angularaxis={'tickfont_size': 10, 'tickfont_weight': 'normal'})
fig.update_polars(radialaxis={'range': [0, 1], 'dtick': 0.2, 'showticklabels': False})
fig.update_layout(template=None)
fig.show()