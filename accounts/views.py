from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import SignUpForm
from .models import Profile


def signup(request):
    if request.user.is_authenticated:
        return redirect("storefront:home")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data["first_name"]
            user.save()
            Profile.objects.create(user=user, phone=form.cleaned_data["phone"])
            login(request, user)
            messages.success(request, f"Welcome to Learning Resource Book, {user.first_name}!")
            return redirect("storefront:home")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})
