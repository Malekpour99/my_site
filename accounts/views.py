from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, CustomUserCreationForm
from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse_lazy


def login_view(request):
    redirect_to = request.POST.get("next", request.GET.get("next", "/"))
    if not request.user.is_authenticated:
        if request.method == "POST":
            # form = AuthenticationForm(request=request, data=request.POST)
            form = LoginForm(request.POST)
            if form.is_valid():
                username_or_email = form.cleaned_data.get("username_or_email")
                password = form.cleaned_data.get("password")
                user = authenticate(
                    request, username=username_or_email, password=password
                )
                if user is not None:
                    login(request, user)
                    messages.add_message(
                        request, messages.SUCCESS, f"Welcome, {request.user.username}"
                    )
                    return redirect(redirect_to)
                else:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        "Username or password is incorrect, please try again!",
                    )

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
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                email = form.cleaned_data.get("email")
                user = User.objects.create_user(username, email, password)
                user.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "User has been created Successfully! \nYou can now login.",
                )
                return redirect("/")
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.add_message(
                            request, messages.ERROR, f"{field}: {error}"
                        )

        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "accounts/sign-in.html", context)

    else:
        return redirect("/")


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    # user 'reverse' or 'reverse_lazy' for constructing URLs to prevent security issues!!
    success_url = reverse_lazy("accounts:password_reset_complete")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding uidb64 and token to the template context
        context["uidb64"] = self.kwargs["uidb64"]
        context["token"] = self.kwargs["token"]
        return context
