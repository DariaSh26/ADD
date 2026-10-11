import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd


app = Dash()

df = pd.DataFrame({
    "Продукты": ["Яблоки", "Бананы", "Апельсины"],
    "Цена": [100, 150, 120],
    "В наличии": [True, False, True]
})

app.layout = html.Div([
    dag.AgGrid(
        rowData=df.to_dict("records"),
        columnDefs=[ {'field': i} for i in df.columns],
        defaultColDef={"filter": True, 'floatingFilter': True, 'sortable': True}
    )
])

if __name__ == '__main__':
    app.run(debug=True)

