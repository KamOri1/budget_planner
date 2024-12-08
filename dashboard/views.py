from django.shortcuts import render, redirect


def get_title(request):
    return request.path.strip("/").title()


def main_view(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")
    else:
        return redirect("/login")


def dashboard(request):
    return render(
        request=request,
        template_name="dashboard.html",
        context={"title": get_title(request)},
    )


def billing(request):
    return render(
        request=request,
        template_name="billing.html",
        context={"title": get_title(request)},
    )


def notifications(request):
    return render(
        request=request,
        template_name="notifications.html",
        context={"title": get_title(request)},
    )
