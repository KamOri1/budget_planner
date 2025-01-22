from django.shortcuts import redirect, render

from .utils.today_money import TodayMoney


def get_title(request):
    return request.path.strip("/").title()


def main_view(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")
    else:
        return redirect("/login")


def dashboard(request):
    today_profit = TodayMoney()

    context = {
        "today_profit": today_profit.today_profit,
        "monthly_income": today_profit.sum_of_profit(),
        "monthly_expenses": today_profit.sum_of_expenses(),
    }
    return render(request=request, template_name="dashboard.html", context=context)


def billing(request):
    return render(
        request=request,
        template_name="billing.html",
    )


def notifications(request):
    return render(
        request=request,
        template_name="notifications.html",
    )
