import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
print(df.columns)

app = Dash()

app.layout = [
    html.Div(children=["Мое приложение с использованием Dash"]),
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{'field': i} for i in df.columns]
    ),
    dcc.Graph(figure = px.histogram(df, x="continent", y="lifeExp", histfunc="avg")),
]

if __name__ == '__main__':
    app.run(debug=True)