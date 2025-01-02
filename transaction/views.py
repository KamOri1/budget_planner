from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import UpdateTransactionForm
from .models import Transaction


class TransactionHomeView(TemplateView):
    template_name = "transaction/transaction_home_page.html"


class TransactionCreateView(CreateView):
    model = Transaction
    fields = ["transaction_name", "sum_amount", "description", "category_id"]
    template_name = "transaction/transaction_add.html"
    success_url = "create_transaction"

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user_id_id = self.request.user.id
        form.save()

        return redirect(self.success_url)


class TransactionListView(ListView):
    model = Transaction
    template_name = "transaction/transaction_list.html"
    context_object_name = "transactions"
    ordering = ["-transaction_name"]

    def get_queryset(self):
        return Transaction.objects.filter(user_id_id=self.request.user).order_by(
            "-transaction_name"
        )


class TransactionUpdateView(UpdateView):
    model = Transaction
    form = UpdateTransactionForm
    fields = ["transaction_name", "sum_amount", "description", "category_id"]
    template_name = "transaction/transaction_update_form.html"
    success_url = "transaction_list"

    def get_queryset(self):
        return Transaction.objects.filter(user_id_id=self.request.user)

    def form_valid(self, form):
        form.save()

        return redirect(self.success_url, q="edit")


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = "transaction/transaction_delete.html"
    success_url = "transaction_list"

    def get_queryset(self):
        return Transaction.objects.filter(user_id_id=self.request.user)

    def form_valid(self, form):
        self.object.delete()

        return redirect(self.success_url, q="del")
