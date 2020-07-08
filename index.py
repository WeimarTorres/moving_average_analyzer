import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State

from pages.homepage import homepage
from pages.bestpage import bestpage
from pages.aboutpage import aboutpage
from pages.errorpage import errorpage

from pages.templates.graph import graph

from pages.logic.movingAverage import calculate_moving_average_crossovers
from pages.logic.checker import checkValues, checkValuesBest
from pages.logic.findBest import findBest

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.config.suppress_callback_exceptions = True
app.title = 'Moving Average Analyzer'

server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return homepage()
    elif pathname == '/best':
        return bestpage()
    elif pathname == '/about':
        return aboutpage()
    else:
        return errorpage()

@app.callback(
    Output('output', 'children'),
    [Input('button', 'n_clicks')],
    [State('symbol', 'value'),
    State('days', 'value'),
    State('money', 'value'),
    State('ma1', 'value'),
    State('ma2', 'value'),
    State('timeframe', 'value')])
def update_output(n_clicks, symbol, nDays, money, ma1, ma2, timeframe):
    checker = checkValues(symbol, nDays, money, ma1, ma2)
    if(checker[0]):
        data = calculate_moving_average_crossovers(symbol, timeframe, nDays, ma1, ma2, money)
        if not(type(data[0]) is int):
            return graph(data, symbol, ma1, ma2, money)
        else:
            return dbc.Container(
                [
                    dbc.Row(
                        [
                            html.P(
                                'Database Error',
                                className="lead",
                            ),
                        ], justify="center", align="center"
                    )
                ]
            )
    else:
        return dbc.Container(
            [
                dbc.Row(
                    [
                        html.P(
                            checker[1],
                            className="lead",
                        ),
                    ], justify="center", align="center"
                )
            ]
        )

@app.callback(
    [Output('outputBest1', 'children'),
     Output('outputBest2', 'children')],
    [Input('buttonBest', 'n_clicks')],
    [State('daysBest', 'value'),
    State('moneyBest', 'value'),
    State('ma1Best', 'value'),
    State('ma2Best', 'value'),
    State('timeframeBest', 'value')])
def update_output_best(n_clicks, nDays, money, ma1, ma2, timeframe):
    checker = checkValuesBest(nDays, money, ma1, ma2)
    if(checker[0]):
        data = findBest(timeframe, nDays, ma1, ma2, money)
        if not(type(data[0][1][0]) is int) and not(type(data[1][1][0]) is int):
            return graph(data[0][1], data[0][0], ma1, ma2, money), graph(data[1][1], data[1][0], ma1, ma2, money)
        else:
            return dbc.Container(
                [
                    dbc.Row(
                        [
                            html.P(
                                'Database Error',
                                className="lead",
                            ),
                        ], justify="center", align="center"
                    )
                ]
            )
    else:
        return dbc.Container(
            [
                dbc.Row(
                    [
                        html.P(
                            checker[1],
                            className="lead",
                        ),
                    ], justify="center", align="center"
                )
            ]
        ), dbc.Container(
            [
                dbc.Row(
                    [
                        html.P(
                            checker[1],
                            className="lead",
                        ),
                    ], justify="center", align="center"
                )
            ]
        )

if __name__ == '__main__':
    app.run_server()