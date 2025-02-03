from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import CreateView, View

from .forms import UserLoginForm, UserRegisterForm
from .token import account_activation_token


class ActiveView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(
                self.request, "Your account has been confirmed. You can now login."
            )
            return redirect(reverse_lazy("login"))
        else:
            messages.error(self.request, "Activation link is invalid.")

        return redirect(reverse_lazy("register"))


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        self._activate_email(user, user.email)

        return redirect(self.success_url)

    def form_invalid(self, form):

        return self.render_to_response(self.get_context_data(form=form))

    def _activate_email(self, user, to_email):
        mail_subject = "Activate your Budget Planner account."
        message = render_to_string(
            "users/template_activate_account.html",
            {
                "user": user.username,
                "domain": get_current_site(self.request).domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user),
                "protocol": "https" if self.request.is_secure() else "http",
            },
        )
        email = EmailMessage(mail_subject, message, to=[to_email])
        if email.send():
            messages.success(
                self.request, f"{user} Activate your email account. {to_email}"
            )
        else:
            messages.error(
                self.request,
                f"Problem sending email to {to_email}, check if your typed it correctly",
            )


class LoginView(DjangoLoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("dashboard")


class LogoutView(View):
    @staticmethod
    def post(request):
        logout(request)
        messages.success(request, "you been logged out.")
        return redirect("login")
