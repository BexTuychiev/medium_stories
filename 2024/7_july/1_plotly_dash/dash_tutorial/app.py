from dash import Dash, html

app = Dash()

app.layout = html.Div([html.H1("Hello, Dash!"), html.Div("My first Dash app.")])

if __name__ == "__main__":
    app.run(debug=True)
