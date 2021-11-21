import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label{}'.format(i) for i in range(10)},
        value=5,
    )
], style={"width": 500})

if __name__ == '__main__':
    app.run_server(debug=True)