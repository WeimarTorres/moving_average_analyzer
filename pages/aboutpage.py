import dash_bootstrap_components as dbc
import dash_html_components as html

from .templates.navbar import navbar

navbar = navbar()
about = dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.H1("ABOUT", className="display-3"),
                html.P(
                    "This project has the purpose of being able to analyze the benefits that would be obtained by being able to invent with a bot using moving averages as an indicator for buying or selling",
                    className="lead",
                ),
                html.P(
                    "Data is obtained from ALPACA API Stock Brokerage.",
                    className="lead",
                ),
                html.A("https://alpaca.markets/", href="https://alpaca.markets/", className="alert-link"),
            ],
            fluid=True,
        )
    ],
    fluid=True,
)

def aboutpage():
    layout = html.Div([
        navbar,
        about
    ])

    return layout