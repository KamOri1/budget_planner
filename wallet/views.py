from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from .filters import WalletFilter
from .forms import UpdateWalletForm
from .models import Wallet


class WalletHomeView(TemplateView):
    template_name = "wallet/wallet_home_page.html"


class WalletCreateView(CreateView):
    model = Wallet
    fields = ["name", "portfolio_value"]
    template_name = "wallet/wallet_add.html"
    success_url = "wallet-home"

    def form_valid(self, form):
        wallet = form.save(commit=False)
        wallet.user_id = self.request.user.id
        form.save()

        return redirect(self.success_url)


class WalletListView(ListView):
    paginate_by = 10
    queryset = Wallet.objects.all()
    template_name = "wallet/wallet_home_page.html"
    context_object_name = "wallets"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = WalletFilter(self.request.GET, queryset=queryset)

        if not self.filterset.qs.query.order_by:
            queryset = self.filterset.qs.order_by("-portfolio_value")
        else:
            queryset = self.filterset.qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        if Wallet.objects.filter(user=self.request.user):
            return context


class WalletUpdateView(UpdateView):
    model = Wallet
    form = UpdateWalletForm
    fields = ["name", "portfolio_value"]
    template_name = "wallet/wallet_update_form.html"
    success_url = "wallet-home"

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.save()

        return redirect(self.success_url)


class WalletDeleteView(DeleteView):
    model = Wallet
    template_name = "wallet/wallet_delete.html"
    success_url = "wallet-home"

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)

    def form_valid(self, form):
        self.object.delete()

        return redirect(self.success_url)
