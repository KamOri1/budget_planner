from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

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
    model = Notification
    template_name = "notifications/notifications_home_page.html"
    context_object_name = "notifications"
    ordering = ["-name"]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by("-name")


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
