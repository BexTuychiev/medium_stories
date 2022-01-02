import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import seaborn as sns

app = dash.Dash(__name__)

diamonds = sns.load_dataset("diamonds")

scatter = px.scatter(data_frame=diamonds, x="price", y="carat", color="cut",
                     title="Carat vs. Price of Diamonds", width=600, height=400)
histogram = px.histogram(data_frame=diamonds, x='price', title="Histogram of Diamond prices", width=600, height=400)
violin = px.violin(data_frame=diamonds, x="cut", y="price", title="Violin Plot of Cut vs. Price", width=600, height=400)

left_fig = html.Div(children=dcc.Graph(figure=scatter))
right_fig = html.Div(children=dcc.Graph(figure=histogram))

upper_div = html.Div([left_fig, right_fig], style={"display": "flex"})
central_div = html.Div(children=dcc.Graph(figure=violin), style={"display": "flex", "justify-content": "center"})
app.layout = html.Div([upper_div, central_div])

if __name__ == '__main__':
    app.run_server(debug=True)
