from django.shortcuts import render
from django.views.generic import TemplateView


def billing(request):
    return render(
        request=request,
        template_name="billings/billing_home_page.html",
    )


class BillingView(TemplateView):
    template_name = "billings/billing_home_page.html"
