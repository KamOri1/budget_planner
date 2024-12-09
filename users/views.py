from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


def register(request):  # TODO Class Based View + Template z boostrap'a.
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Dear {username}, you been successfully sign up."
            )
            return redirect("/login")
    else:
        form = UserRegisterForm()

    return render(request, "users/sign-up.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "you been log out.")
    return redirect("/login")
