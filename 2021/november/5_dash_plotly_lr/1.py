import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(name="app")

# Load dataset using Plotly
tips = px.data.tips()

fig = px.scatter(tips, x="total_bill", y="tip")  # Create a scatterplot

title = html.H1("Hello Dash!")
text_div = html.Div("Dash: A web application framework for your data.")
graph_to_display = dcc.Graph(id="scatter", figure=fig)

app.layout = html.Div(children=[title, text_div, graph_to_display])

if __name__ == '__main__':
    app.run_server(debug=True)
