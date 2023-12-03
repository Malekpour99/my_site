from django.shortcuts import render

# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        msg = f"User is logged in as {request.user.username}"
    else:
        msg = "User in not logged in!"

    return render(request, "accounts/login.html", {"msg": msg})


# def logout_view(request):
# pass


def signin_view(request):
    pass
