import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(name="app")

app.layout = html.Div(
    children=html.H3("Simple Div"),
    id="sample_div",
    className="red_div",
    style={"backgroundColor": "red"},
)

if __name__ == '__main__':
    app.run_server(debug=True)
