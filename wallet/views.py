from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView

from wallet.models import Wallet

from .forms import UpdateWalletForm


class WalletCreateView(CreateView):
    model = Wallet
    fields = ["wallet_name", "portfolio_value"]
    template_name = "wallet/wallet_add.html"
    success_url = "create_wallet"

    def form_valid(self, form):
        wallet = form.save(commit=False)
        wallet.user_id_id = self.request.user.id
        form.save()

        return redirect(self.success_url)


class WalletListView(ListView):
    model = Wallet
    template_name = "wallet/wallet_home_page.html"
    context_object_name = "wallets"
    ordering = ["-portfolio_value"]


class WalletUpdateView(UpdateView):
    model = Wallet
    form = UpdateWalletForm
    fields = ["wallet_name", "portfolio_value"]
    template_name = "wallet/wallet_update.html"
    success_url = "wallet-home"

    def form_valid(self, form):
        form.save()

        return redirect(self.success_url)


class WalletSelectView(ListView):
    model = Wallet
    fields = ["wallet_name", "portfolio_value", "wallet_id"]
    template_name = "wallet/wallet_update.html"
    success_url = "update_wallet"

    def form_valid(self, form):
        wallet = form.save(commit=False)
        wallet.user_id_id = self.request.user.id
        form.save()

        return redirect(self.success_url)
