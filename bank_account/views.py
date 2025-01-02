from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import UpdateAccountForm
from .models import BankAccount


class AccountCreateView(CreateView):
    model = BankAccount
    fields = ["account_name", "account_number", "sum_of_funds"]
    template_name = "bank_account/account_add.html"
    success_url = "account-home"

    def form_valid(self, form):
        account = form.save(commit=False)
        account.user_id_id = self.request.user.id
        form.save()

        return redirect(self.success_url)


class AccountListView(ListView):
    model = BankAccount
    template_name = "bank_account/account_home_page.html"
    context_object_name = "accounts"
    ordering = ["-account_name"]

    def get_queryset(self):
        return BankAccount.objects.filter(user_id_id=self.request.user).order_by(
            "-account_name"
        )


class AccountUpdateView(UpdateView):
    model = BankAccount
    form = UpdateAccountForm
    fields = ["account_name", "account_number", "sum_of_funds"]
    template_name = "bank_account/account_update_form.html"
    success_url = "account-home"

    def get_queryset(self):
        return BankAccount.objects.filter(user_id_id=self.request.user)

    def form_valid(self, form):
        form.save()

        return redirect(self.success_url)


class AccountDeleteView(DeleteView):
    model = BankAccount
    template_name = "bank_account/account_delete.html"
    success_url = "account-home"

    def get_queryset(self):
        return BankAccount.objects.filter(user_id_id=self.request.user)

    def form_valid(self, form):
        self.object.delete()

        return redirect(self.success_url)
