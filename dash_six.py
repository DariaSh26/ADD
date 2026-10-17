from dash import Dash, html, dcc,  callback, Input, Output
import pandas as pd
import plotly.express as px

app=Dash()

df= pd.DataFrame({
    "Fruit": ["Яблоки", "Апельсины", "Бананы", "Яблоки", "Апельсины", "Бананы"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["Сочи", "Сочи", "Сочи", "Москва", "Москва", "Москва"]
})

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


app.layout = html.Div(children=[
    html.H1(children='Столбчатая диаграмма'),

    html.Div(children="При клике на название города в легенде справа, можно скрыть или показать столбцы на графике"),

    html.Br(),

    html.Div([
        html.Label("выберите город для фильтрации:"),
        dcc.Dropdown(
            id="city-dropdown",
            options=[
                {'label': 'Все города', "value": "All"},
                {'label': 'Сочи', "value": "Сочи"},
                {'label': 'Москва', "value": "Москва"},
            ],
            value="All",
        )
    ], style={'width': '300px', "margin": "10px 0"}),

    dcc.Graph(
        id='example-graph',
        # figure=fig
    )
])

@app.callback(
    Output('example-graph', 'figure'),
    [Input('city-dropdown', 'value')]
)
def update_graph(selected_city):
    if selected_city == "All":
        filtered_df = df
    else:
        filtered_df = df[df['City'] == selected_city]

    fig = px.bar(filtered_df, x="Fruit", y="Amount", color="City", barmode="group")
    fig.update_yaxes(range=[0, 6])
    return fig


if __name__ == '__main__':
    app.run(debug=True)