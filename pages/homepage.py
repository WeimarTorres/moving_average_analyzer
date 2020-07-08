import dash_html_components as html

from .templates.navbar import navbar
from .templates.inputData import inputData

navbar = navbar()
inputData = inputData()
output = html.Div(
    id = 'output',
    children = [],
)

def homepage():
    layout = html.Div([
        navbar,
        inputData,
        output
    ])

    return layout