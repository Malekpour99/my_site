from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.


def login_view(request):
    redirect_to = request.POST.get('next', request.GET.get('next', '/'))
    if not request.user.is_authenticated:
        if request.method == "POST":
            # form = AuthenticationForm(request=request, data=request.POST)
            form = LoginForm(request.POST)
            if form.is_valid():
                username_or_email = form.cleaned_data.get("username_or_email")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username_or_email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(redirect_to)

        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)

    else:
        return redirect(redirect_to)

@login_required
def logout_view(request):
    logout(request)
    return redirect("/")


def signin_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/")

        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "accounts/sign-in.html", context)

    else:
        return redirect("/")
