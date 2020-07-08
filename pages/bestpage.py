import dash_html_components as html
import dash_bootstrap_components as dbc

from .templates.navbar import navbar
from .templates.inputData import inputDataBest

navbar = navbar()
inputData = inputDataBest()
output = dbc.Row(
    [
        dbc.Col(
            [
                html.Div(
                    id = 'outputBest1',
                    children = [],
                )
            ]
        ),
        dbc.Col(
            [
                html.Div(
                    id = 'outputBest2',
                    children = [],
                )
            ]
        )
    ]
)

def bestpage():
    layout = html.Div([
        navbar,
        inputData,
        output
    ])

    return layout