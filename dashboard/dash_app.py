import pandas as pd
import plotly.express as px
from dash import Input, Output, dcc, html
from django_plotly_dash import DjangoDash

from dashboard.utils.today_transactions import TodayTransactions

app = DjangoDash("Dailytransactions")


app.layout = html.Div(
    [
        dcc.Graph(id="example"),
    ],
)


@app.callback(Output("example", "figure"), Input("example", "id"))
def update_output(_, *args, **kwargs):
    user = kwargs["user"]
    transactions = TodayTransactions(user=user)
    daily_transactions = pd.DataFrame(transactions.daily_transactions())
    daily_transactions = daily_transactions.drop_duplicates(
        subset=["name"], keep="first"
    )

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
        color="Name",
        color_discrete_map=transactions.transaction_color(),
        title="Daily transactions",
    )
    fig.update_layout(
        xaxis_tickangle=45,
        xaxis=dict(tickfont=dict(size=9)),
        showlegend=False,
        bargap=0,
    )
    return fig
