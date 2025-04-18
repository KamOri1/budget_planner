from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .filters import AccountFilter
from .forms import UpdateAccountForm
from .models import BankAccount


class AccountCreateView(CreateView):
    model = BankAccount
    fields = ["name", "number", "sum_of_funds"]
    template_name = "bank_account/account_add.html"
    success_url = "home_account"

    def form_valid(self, form):
        account = form.save(commit=False)
        account.user_id_id = self.request.user.id
        form.save()

        return redirect(self.success_url)


class AccountListView(ListView):
    paginate_by = 10
    queryset = BankAccount.objects.all()
    template_name = "bank_account/account_home_page.html"
    context_object_name = "accounts"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AccountFilter(self.request.GET, queryset=queryset)

        if not self.filterset.qs.query.order_by:
            queryset = self.filterset.qs.order_by("-name")
        else:
            queryset = self.filterset.qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        if BankAccount.objects.filter(user=self.request.user):
            return context


class AccountUpdateView(UpdateView):
    model = BankAccount
    form = UpdateAccountForm
    fields = ["name", "number", "sum_of_funds"]
    template_name = "bank_account/account_update_form.html"
    success_url = "home_account"

    def get_queryset(self):
        return BankAccount.objects.filter(user_id=self.request.user)

    def form_valid(self, form):
        form.save()

        return redirect(self.success_url)


class AccountDeleteView(DeleteView):
    model = BankAccount
    template_name = "bank_account/account_delete.html"
    success_url = "home_account"

    def get_queryset(self):
        return BankAccount.objects.filter(user_id=self.request.user)

    def form_valid(self, form):
        self.object.delete()

        return redirect(self.success_url)
