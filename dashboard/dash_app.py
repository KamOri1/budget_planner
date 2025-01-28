import pandas as pd
import plotly.express as px
from dash import dcc, html
from django_plotly_dash import DjangoDash

from dashboard.utils.today_transactions import TodayTransactions

app = DjangoDash("SimpleExample")

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

transactions = TodayTransactions()
daily_transactions = pd.DataFrame(transactions.daily_transactions())
daily_transactions = daily_transactions.drop_duplicates(subset=["name"], keep="first")
print(daily_transactions["name"])
print(daily_transactions["value"])
print(daily_transactions["type"])
print(transactions.transaction_color())

df = pd.DataFrame(
    {
        "Name": daily_transactions["name"],
        "Values": daily_transactions["value"],
    }
)


fig = px.bar(
    df,
    x="Name",
    y="Values",
    barmode="group",
    color_discrete_map=transactions.transaction_color(),
)

app.layout = html.Div(
    children=[
        dcc.Graph(
            id="example-graph", figure=fig, style={"width": "100%", "height": "100%"}
        ),
    ]
)
