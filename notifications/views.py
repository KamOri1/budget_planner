from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .filters import NotificationFilter
from .forms import CreateNotificationForm, UpdateNotificationForm
from .models import Notification


class NotificationCreateView(CreateView):
    model = Notification
    form_class = CreateNotificationForm
    template_name = "notifications/notifications_add.html"
    success_url = reverse_lazy("notification_home")

    def form_valid(self, form):
        expenses = form.save(commit=False)
        expenses.user_id = self.request.user.id
        form.save()

        return super().form_valid(form)


class NotificationListView(ListView):
    paginate_by = 10
    queryset = Notification.objects.all()
    template_name = "notifications/notifications_home_page.html"
    context_object_name = "notifications"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NotificationFilter(self.request.GET, queryset=queryset)

        if not self.filterset.qs.query.order_by:
            queryset = self.filterset.qs.order_by("-name")
        else:
            queryset = self.filterset.qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        if Notification.objects.filter(user_id=self.request.user):
            return context


class NotificationUpdateView(UpdateView):
    model = Notification
    form_class = UpdateNotificationForm
    template_name = "notifications/notifications_update_form.html"
    success_url = "notification_home"

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.save()

        return redirect(self.success_url)


class NotificationDeleteView(DeleteView):
    model = Notification
    template_name = "notifications/notifications_delete.html"
    success_url = reverse_lazy("notification_home")

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    def form_valid(self, form):
        self.object.delete()

        return redirect(self.success_url)
