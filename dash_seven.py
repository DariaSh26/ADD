from dash import Dash, html, dcc,  callback, Input, Output
import pandas as pd
import plotly.express as px

app = Dash()

data = {
    "Month": ["Январь", "Февраль", "март", " Апрель", "Май", "Июнь"]* 3,
    "Category": (["Электроника"] * 6) + (["Одежда"] * 6) + (["Продукты"] * 6),
    "Revenue": [
        150, 180, 220, 190, 250, 300, # Электроника
        80, 95, 130, 110, 105, 90, # Одежда
        200, 210, 230, 225, 240, 260 # Продукты
    ],
    "Quantity": [
        50, 60, 75, 62, 80, 95,  # Электроника
        160, 190, 260, 220, 210, 180, # Одежда
        1000, 1050, 1150, 1120, 1200, 1300   # Продукты
    ]
}

df = pd.DataFrame(data)
df["Avg_Check"] = round(df["Revenue"] * 1000 / df["Quantity"], 1)

metrics_labels = {
    "Revenue": "Выручка (тыс. руб.)",
    "Quantity": "количество продаж (шт.)",
    "Avg_Check": "Средний чек (руб.)"
}

app.layout = html.Div(
    style={"padding": "20px", 'font-family': 'Arial, sans-serif'},
    children=[
        html.H1("Аналитический дашборд продаж", style={"color": "#2c3e50"}),
        html.Div("Интерактивный анализ ключевых показателей эффективности (KPI) по категориям товаров"),
        html.Br(),
        html.Div([
            html.Label("выберите аналитическую метрику:", style={"fontWeight": "bold", "marginBottom": "8px", "display": "block"}),
            dcc.Dropdown(
                id="metric-dropdown",
                options=[
                    {"label": "Финансовая выручка", "value": "Revenue"},
                    {"label": "Объем продаж (в штуках)", "value": "Quantity"},
                    {"label": "Размер среднего чека", "value": "Avg_Check"},
                ],
                value="Revenue",
                clearable=False,
            )
        ], style={"width": "350px", "backgroundColor": "#f8f9fa", "padding": "15px", "borderRadius": "5px"}),
        html.Br(),

        dcc.Graph(id="analytics-graph")
    ]
)

@app.callback(
    Output("analytics-graph", "figure"),
    Input("metric-dropdown", "value"),
)
def update_trend_graph(selected_metric):
    fig = px.line(
        df,
        x="Month",
        y=selected_metric,
        color="Category",
        markers=True,
        title=f"Динамика показателя: {metrics_labels[selected_metric]}",
        labels={selected_metric: metrics_labels[selected_metric], "Month": "Месяц", "Category": "Категория"},
    )

    fig.update_layout(
        hovermode="x unified",
        # plot_bgcolor="white",
        margin={"r": 40, "t": 50, "l": 40, "b": 40},
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
