import dash_bootstrap_components as dbc

def navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Analyze", href="/")),
            dbc.NavItem(dbc.NavLink("Find the best", href="/best")),
            dbc.NavItem(dbc.NavLink("About", href="/about"))
        ],
        brand="Moving Average Analyzer",
        brand_href="/",
        color="primary",
        dark=True,
    )

    return navbar