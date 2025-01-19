from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .filters import PossessionStatusFilter
from .forms import CreatePossessionStatusForm, UpdatePossessionStatusForm
from .models import PossessionStatus


class PossessionsCreateView(CreateView):
    model = PossessionStatus
    form_class = CreatePossessionStatusForm
    template_name = "possession_status/possession_add.html"
    success_url = reverse_lazy("possessions_home")

    def form_valid(self, form):
        expenses = form.save(commit=False)
        expenses.user_id = self.request.user.id
        form.save()

        return super().form_valid(form)


class PossessionsListView(ListView):
    paginate_by = 10
    queryset = PossessionStatus.objects.all()
    template_name = "possession_status/possession_home_page.html"
    context_object_name = "possessions"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PossessionStatusFilter(self.request.GET, queryset=queryset)

        if not self.filterset.qs.query.order_by:
            queryset = self.filterset.qs.order_by("-asset_name")
        else:
            queryset = self.filterset.qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        if PossessionStatus.objects.filter(user_id=self.request.user):
            return context


class PossessionsUpdateView(UpdateView):
    model = PossessionStatus
    form_class = UpdatePossessionStatusForm
    template_name = "possession_status/possession_update_form.html"
    success_url = "possessions_home"

    def get_queryset(self):
        return PossessionStatus.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.save()

        return redirect(self.success_url)


class PossessionsDeleteView(DeleteView):
    model = PossessionStatus
    template_name = "possession_status/possession_delete.html"
    success_url = reverse_lazy("possessions_home")

    def get_queryset(self):
        return PossessionStatus.objects.filter(user=self.request.user)

    def form_valid(self, form):
        self.object.delete()

        return redirect(self.success_url)
