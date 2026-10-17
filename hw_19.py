from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()

data = {
    "Товары": ['Ноутбук', 'Смартфон', 'Планшет', 'Часы', 'Фотоаппарат'],
    "Продажи": [120, 250, 180, 90, 150]
}
df = pd.DataFrame(data)

app.layout = [
    html.Div(children=["Переключение графиков"]),
    html.Hr(),
    dcc.RadioItems(options=[
                   {'label': 'Столбчатая диаграмма', 'value': 'bar'},
                   {'label': 'Линейный график', 'value': 'line'}
        ],
        value='bar',
        id='controls-and-radio-item'
    ),
    dcc.Graph(figure = {}, id="controls-and-graph")
]

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(chart_type_chosen):
    if chart_type_chosen == 'bar':
       fig = px.bar(df, x="Товары", y="Продажи", title="Анализ продаж товаров")
    else:
       fig = px.line(df, x="Товары", y="Продажи", title="Динамика продаж товаров")

    return fig

if __name__ == '__main__':
    app.run(debug=True)

