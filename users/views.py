from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegisterForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, f"Account created for {user.username}")
        return super().form_valid(form)


# def register(request):  # TODO Class Based View + Template z boostrap'a.
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             messages.success(
#                 request, f"Dear {username}, you been successfully sign up."
#             )
#             return redirect("/login")
#     else:
#         form = UserRegisterForm()
#
#     return render(request, "users/register.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "you been log out.")
    return redirect("login")
