from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView as login_view
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import UserRegisterForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, f"Account created for {user.username}")
        return redirect(self.success_url)

    def form_invalid(self, form):

        return self.render_to_response(self.get_context_data(form=form))


class LoginView(login_view):
    template_name = "users/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("dashboard")


class LogoutView(generic.View):
    @staticmethod
    def get(request):
        logout(request)
        messages.success(request, "you been logged out.")
        return redirect("login")
