import dash_bootstrap_components as dbc
import dash_html_components as html

from .templates.navbar import navbar

navbar = navbar()
error = dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.H1("404", className="display-3"),
                html.P(
                    "The requested URL was not found on this server.",
                    className="lead",
                ),
            ],
            fluid=True,
        )
    ],
    fluid=True,
)

def errorpage():
    layout = html.Div([
        navbar,
        error
    ])

    return layout