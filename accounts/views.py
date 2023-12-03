from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, "accounts/login.html")


# def logout_view(request):
# pass


def signin_view(request):
    pass
