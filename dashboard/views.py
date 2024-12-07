from django.shortcuts import render


def get_title(request):
    return request.path.strip("/").title()


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
