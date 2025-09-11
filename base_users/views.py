from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("myusers:profile")
    else:
        form = SignUpForm()
    return render(request, "myusers/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("myusers:profile")
    else:
        form = LoginForm()
    return render(request, "myusers/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("myusers:login")

@login_required
def profile_view(request):
    return render(request, "myusers/profile.html", {"user": request.user})
