import dash_html_components as html
import dash_bootstrap_components as dbc

def inputData():
    inputData = dbc.Jumbotron(
        [
            html.H1("Data", className="display-3"),
            html.P(
                "Information for analysis.",
                className="lead",
            ),
            html.Hr(className="my-2"),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("SYMBOL", addon_type="prepend"),
                                    dbc.Input(id="symbol", placeholder="Insert a Symbol", type="text", value="AAPL"),
                                ]
                            ),
                            dbc.FormText("All with capital letters", className="mb-3"),
                        ],
                    ),
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Days", addon_type="prepend"),
                                    dbc.Input(id="days", placeholder="Insert the number of days", type="number", value=360),
                                ],
                                className="mb-3",
                            ),
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Money", addon_type="prepend"),
                                    dbc.Input(id="money", placeholder="Insert the initial amount of money in dollars", type="number", value=100),
                                ],
                                className="mb-3",
                            ),
                        ]
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("1st Moving Average", addon_type="prepend"),
                                    dbc.Input(id="ma1", placeholder="Insert the number of moving average 1", type="number", value=20),
                                ],
                                className="mb-3",
                            ),
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("2nd Moving Average", addon_type="prepend"),
                                    dbc.Input(id="ma2", placeholder="Insert the number of moving average 2", type="number", value=100),
                                ],
                                className="mb-3",
                            ),
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Time Frame", addon_type="prepend"),
                                    dbc.Select(
                                        id="timeframe",
                                        options=[
                                            {"label": "1 Minute", "value": "1Min"},
                                            {"label": "5 Minutes", "value": "5Min"},
                                            {"label": "15 Minutes", "value": "15Min"},
                                            {"label": "1 Day", "value": "1D"},
                                        ],
                                        value="1D"
                                    ),
                                ],
                                className="mb-3",
                            ),
                        ]
                    )
                ]
            ),
            html.P(dbc.Button("Analyze", id="button", color="primary"), className="lead"),
        ]
    )

    return inputData

def inputDataBest():
    inputData = dbc.Jumbotron(
        [
            html.H1("Data", className="display-3"),
            html.P(
                "Information for analysis.",
                className="lead",
            ),
            html.Hr(className="my-2"),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Days", addon_type="prepend"),
                                    dbc.Input(id="daysBest", placeholder="Insert the number of days", type="number", value=360),
                                ],
                                className="mb-3",
                            ),
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Money", addon_type="prepend"),
                                    dbc.Input(id="moneyBest", placeholder="Insert the initial amount of money in dollars", type="number", value=100),
                                ],
                                className="mb-3",
                            ),
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Time Frame", addon_type="prepend"),
                                    dbc.Select(
                                        id="timeframeBest",
                                        options=[
                                            {"label": "1 Minute", "value": "1Min"},
                                            {"label": "5 Minutes", "value": "5Min"},
                                            {"label": "15 Minutes", "value": "15Min"},
                                            {"label": "1 Day", "value": "1D"},
                                        ],
                                        value="1D"
                                    ),
                                ],
                                className="mb-3",
                            ),
                        ]
                    )
                ]
            ),
            dbc.Row(
                [
                    html.P(dbc.Button("Analyze", id="buttonBest", color="primary"), className="lead"),
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("1st Moving Average", addon_type="prepend"),
                                    dbc.Input(id="ma1Best", placeholder="Insert the number of moving average 1", type="number", value=20),
                                ],
                                className="mb-3",
                            ),
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("2nd Moving Average", addon_type="prepend"),
                                    dbc.Input(id="ma2Best", placeholder="Insert the number of moving average 2", type="number", value=100),
                                ],
                                className="mb-3",
                            ),
                        ]
                    ),
                ]
            ),
        ]
    )

    return inputData