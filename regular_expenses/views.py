from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CreateRegularExpensesForm, UpdateRegularExpensesForm
from .models import RegularExpenses


class RegularExpensesCreateView(CreateView):
    model = RegularExpenses
    form_class = CreateRegularExpensesForm
    template_name = "regular_expenses/expenses_add.html"
    success_url = reverse_lazy("expenses_home")

    def form_valid(self, form):
        expenses = form.save(commit=False)
        expenses.user_id = self.request.user.id
        form.save()

        return super().form_valid(form)


class RegularExpensesListView(ListView):
    model = RegularExpenses
    template_name = "regular_expenses/expenses_home_page.html"
    context_object_name = "expenses"
    ordering = ["-name"]

    def get_queryset(self):
        return RegularExpenses.objects.filter(user=self.request.user).order_by("-name")


class RegularExpensesUpdateView(UpdateView):
    model = RegularExpenses
    form_class = UpdateRegularExpensesForm
    template_name = "regular_expenses/expenses_update_form.html"
    success_url = "expenses_home"

    def get_queryset(self):
        return RegularExpenses.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.save()

        return redirect(self.success_url)


class RegularExpensesDeleteView(DeleteView):
    model = RegularExpenses
    template_name = "regular_expenses/expenses_delete.html"
    success_url = reverse_lazy("expenses_home")

    def get_queryset(self):
        return RegularExpenses.objects.filter(user=self.request.user)

    def form_valid(self, form):
        self.object.delete()

        return redirect(self.success_url)
