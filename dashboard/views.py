from django.shortcuts import redirect, render


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
    )


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
