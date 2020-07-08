import dash_core_components as dcc
import plotly.graph_objs as go

def graph(data, st, ma1, ma2, money):
    graph = dcc.Graph(
        id='scatter_chart',
        figure = {
            'data': [
                go.Scatter(
                    x = data[0]['Date'],
                    y = data[0]['Close Price'],
                    name = '%s Closing Price' % st
                ),
                go.Scatter(
                    x = data[0]['Date'],
                    y = data[1],
                    name = 'Moving Average %s Days' % ma1,
                    marker={
                        'color': 'orange'
                    }
                ),
                go.Scatter(
                    x = data[0]['Date'],
                    y = data[2],
                    name = 'Moving Average %s Days' % ma2,
                    marker={
                        'color': 'purple'
                    }
                ),
                go.Scatter(
                    x = data[3]['Date'],
                    y = data[3]['Price'],
                    name = 'Buy',
                    mode = 'markers',
                    marker={
                        'color': 'green',
                        'size': 10
                    }
                ),
                go.Scatter(
                    x = data[4]['Date'],
                    y = data[4]['Price'],
                    name = 'Sell',
                    mode = 'markers',
                    marker={
                        'color': 'red',
                        'size': 10
                    }
                )
            ],
            'layout': go.Layout(
                title = '%s, %s -> %s' % (st, money, data[5]),
                xaxis = {'title': 'Dates'},
                yaxis = {'title': 'Closing Price'}
            )
        }
    )

    return graph