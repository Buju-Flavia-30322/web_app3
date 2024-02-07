from django.shortcuts import render, redirect, reverse
from users.forms import RegisterForm


def home_view(request):
    return render(request, 'home.html')
# Create your views here.


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(reverse('home'))

    return render(request, "register.html", {
        "form": form
    })