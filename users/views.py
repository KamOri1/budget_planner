from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from .forms import UserRegisterForm

# def activate_email(request, user, to_email):
#     messages.success(request, f'{user} Activate your email account. {to_email}')
#     print('Activate your email account.')


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        # user = form.save()
        # messages.success(self.request, f"Account created for {user.username}")
        # return redirect(self.success_url)

        # POCZĄTEK kodu autoryzacji email
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        messages.success(self.request, f"{user} Activate your email account.")
        return redirect(self.success_url)

        # KONIEC kodu autoryzacji emiali

    def form_invalid(self, form):

        return self.render_to_response(self.get_context_data(form=form))


class LoginView(DjangoLoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("dashboard")


class LogoutView(View):
    @staticmethod
    def post(request):
        logout(request)
        messages.success(request, "you been logged out.")
        return redirect("login")
