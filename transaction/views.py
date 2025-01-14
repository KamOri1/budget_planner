from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .filters import TransactionFilter
from .forms import CreateTransactionForm, UpdateTransactionForm
from .models import Transaction


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = CreateTransactionForm
    template_name = "transaction/transaction_add.html"
    success_url = reverse_lazy("transaction-home")

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user_id_id = self.request.user.id
        form.save()

        return super().form_valid(form)


# class TransactionListView(ListView):
#     paginate_by = 10
#     queryset = Transaction.objects.all()
#     model = Transaction
#     template_name = "transaction/transaction_home_page.html"
#     context_object_name = "transactions"
#     ordering = ["-transaction_date"]
#
#     def get_queryset(self):
#         return Transaction.objects.filter(user_id=self.request.user).order_by(
#             "-transaction_date"
#         )


class TransactionListView(ListView):
    paginate_by = 5
    queryset = Transaction.objects.all()
    template_name = "transaction/transaction_home_page.html"
    context_object_name = "transactions"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TransactionFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        if Transaction.objects.filter(user_id=self.request.user):
            return context


class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = UpdateTransactionForm
    template_name = "transaction/transaction_update_form.html"
    success_url = "transaction-home"

    def get_queryset(self):
        return Transaction.objects.filter(user_id_id=self.request.user)

    def form_valid(self, form):
        form.save()

        return redirect(self.success_url)


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = "transaction/transaction_delete.html"
    success_url = reverse_lazy("transaction-home")

    def get_queryset(self):
        return Transaction.objects.filter(user_id_id=self.request.user)

    def form_valid(self, form):
        self.object.delete()

        return redirect(self.success_url)
