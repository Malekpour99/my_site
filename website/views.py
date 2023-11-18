from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def index_view(request):
    return render(request, "website/index.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, "website/contact.html", {"form": form})


def about_view(request):
    return render(request, "website/about.html")
