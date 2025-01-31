import pandas as pd
import plotly.express as px
from dash import dcc, html
from django_plotly_dash import DjangoDash

from dashboard.utils.category_compare import CategoryCompare

app_category_compare = DjangoDash("MonthlyCategoryCompare")

compare = CategoryCompare()
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


fig.update_traces(textinfo="percent+value", insidetextorientation="radial")

fig.update_layout(
    showlegend=False,
)
app_category_compare.layout = html.Div(
    children=[
        dcc.Graph(
            id="example-graph",
            figure=fig,
            style={
                "width": "100%",
                "height": "100%",
            },
        ),
    ]
)
