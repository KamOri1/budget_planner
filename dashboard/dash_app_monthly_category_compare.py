import pandas as pd
import plotly.express as px
from dash import Input, Output, dcc, html
from django_plotly_dash import DjangoDash

from dashboard.utils.category_compare import CategoryCompare

app_category_compare = DjangoDash(
    "MonthlyCategoryCompare",
    external_scripts=["https://cdn.plot.ly/plotly-basic-2.18.2.min.js"],
)

app_category_compare.layout = html.Div(
    [
        dcc.Graph(id="example"),
    ]
)


@app_category_compare.callback(Output("example", "figure"), Input("example", "id"))
def update_output(_, *args, **kwargs):
    user = kwargs["user"]
    compare = CategoryCompare(user=user)
    category = pd.DataFrame(compare.compare_category_values())
    df = pd.DataFrame(
        {
            "Name": category["name"],
            "Values": category["value"],
        }
    )
    fig = px.pie(
        df,
        color_discrete_map={"Monthly Profit": "green", "Monthly expenses": "red"},
        names="Name",
        values="Values",
        title="Category Compare",
        hole=0.5,
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )

    fig.update_traces(textinfo="percent", insidetextorientation="radial")

    fig.update_layout(
        showlegend=False,
    )
    return fig
