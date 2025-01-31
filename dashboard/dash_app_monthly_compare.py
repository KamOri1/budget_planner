import pandas as pd
import plotly.express as px
from dash import dcc, html
from django_plotly_dash import DjangoDash

from dashboard.utils.today_money import TodayMoney

app_monthly_compare = DjangoDash("MonthlyCompare")

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

compare = TodayMoney()
data_compare = [
    {"name": "Monthly Profit", "value": compare.sum_of_profit()},
    {"name": "Monthly expenses", "value": compare.sum_of_expenses()},
]
daily_compare = pd.DataFrame(data_compare)


df = pd.DataFrame(
    {
        "Name": daily_compare["name"],
        "Values": daily_compare["value"],
    }
)

fig = px.pie(
    df,
    color_discrete_map={"Monthly Profit": "green", "Monthly expenses": "red"},
    names="Name",
    values="Values",
    title="Monthly Compare",
    hole=0.3,
)


fig.update_traces(textinfo="percent+value", insidetextorientation="radial")

fig.update_layout(
    showlegend=False,
)
app_monthly_compare.layout = html.Div(
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
