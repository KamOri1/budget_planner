from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

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
    model = PossessionStatus
    template_name = "possession_status/possession_home_page.html"
    context_object_name = "possessions"
    ordering = ["-asset_name"]

    def get_queryset(self):
        return PossessionStatus.objects.filter(user=self.request.user).order_by(
            "-asset_name"
        )


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
