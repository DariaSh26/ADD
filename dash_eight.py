from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd

data = {
    "Дата": [
        "2026-01",
        "2026-02",
        "2026-03",
        "2026-04",
        "2026-01",
        "2026-02",
        "2026-03",
        "2026-04",
        "2026-01",
        "2026-02",
        "2026-03",
        "2026-04",
    ],
    "Категория": [
        'Электроника',
        'Электроника',
        'Электроника',
        'Электроника',
        'Одежда',
        'Одежда',
        'Одежда',
        'Одежда',
        'Дом',
        'Дом',
        'Дом',
        'Дом'
    ],
    "Продажи": [12000, 15000, 17000, 19000, 8000, 9500, 11000, 10500, 5000, 6200, 7100, 8000],
    "Заказы": [120, 140, 160, 180, 200, 220, 240, 320, 90, 100, 110, 125]
}

df = pd.DataFrame(data)

app = Dash()

app.layout = html.Div(
    children=[html.Div(
        children=[
            html.Label("Выберите категорию товара"),
            dcc.Dropdown(
                id='category-dropdown',
                options=[{
                    "label": "Все категории", "value": "All"
                }]
                        + [{'label': cat, 'value': cat} for cat in df["Категория"].unique()],
                value="All",
                clearable=False,
            )
        ]
    ),
        html.Div(
            children=[
                html.Div(
                    children=[dcc.Graph(id="line-chart")]
                ),
                html.Div(
                    children=[dcc.Graph(id="bar-chart")]
                ),
                html.Div(
                    children=[dcc.Graph(id="pie-chart")]
                )
            ]
        )
    ]
)


@app.callback(
    [
        Output("line-chart", "figure"),
        Output("bar-chart", "figure"),
        Output("pie-chart", "figure")
    ],
    [Input("category-dropdown", "value")],
)
def update_dashboard(selected_category):
    if selected_category == "All":
        filtered_df = df
    else:
        filtered_df = df[df["Категория"] == selected_category]

    fig_line = px.line(
        filtered_df,
        x="Дата",
        y="Продажи",
        color="Категории",
        markers=True,
        title="Динамика продаж по месяцам"
    )

    for fig in [fig_line]:
        fig.update_layout(
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            lrgend={"orientation": "h", "y": -0.2},
        )

    return fig_line


if __name__ == '__main__':
    app.run(debug=True)
