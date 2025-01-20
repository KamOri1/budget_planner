from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .filters import RegularExpensesFilter
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
    paginate_by = 10
    queryset = RegularExpenses.objects.all()
    template_name = "regular_expenses/expenses_home_page.html"
    context_object_name = "expenses"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = RegularExpensesFilter(self.request.GET, queryset=queryset)

        if not self.filterset.qs.query.order_by:
            queryset = self.filterset.qs.order_by("-name")
        else:
            queryset = self.filterset.qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        if RegularExpenses.objects.filter(user_id=self.request.user):
            return context


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
