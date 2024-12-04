from django.shortcuts import render


def dashboard(request):
    return render(request=request, template_name="dashboard.html")


def base(request):
    return render(request=request, template_name="base.html")
