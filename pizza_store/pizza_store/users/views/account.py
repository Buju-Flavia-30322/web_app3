from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect,reverse
from users.forms import RegisterForm



AuthUser = get_user_model()


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "register.html", {
        "form": form
    })