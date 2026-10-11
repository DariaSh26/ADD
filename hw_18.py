
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px


x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

df = pd.DataFrame({'x': x, 'y': y})

app = Dash()

fig = px.line(df, x='x', y='y', title='График функции y = x²', markers=True)

app.layout = html.Div([
    html.H1(children=["Мой первый дашборд"]),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)