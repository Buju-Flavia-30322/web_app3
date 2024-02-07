from django.core.mail import send_mail, EmailMultiAlternatives  # pt mail
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, reverse  # redirectioneaza la home page creca
from django.template.loader import get_template  # tot la pasul cu email importat

from rest_framework import viewsets
from rest_framework.response import Response

from hr.models import Employer
from hr.forms import UserImageForm
from hr.forms import RegisterForm
from hr.serializers import RegisterSerializer

AuthUserModel = get_user_model()


# Create your views here.
def HomePage_view(request):
    return render(request, 'HomePage.html')


def contact_view(request):
    return render(request, 'contact.html', {
        'message': 'acesta este un mesaj dinamic venit de la server'
    })


def employer_view(request):
    all_employwers_qs = Employer.objects.all()
    print("!! all_employers_sg: ", all_employwers_qs)

    return render(request, 'employers.html', {
        'employers': all_employwers_qs
    })


def upload_view(request):
    if request.method == "GET":
        form = UserImageForm()
    else:
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect(reverse("home"))

    return render(request, "upload.html", {
        'form': form
    })


def send_email_view(request):
    first_employer = Employer.objects.first()
    context = {
        'first_name': 'Flavia',
        'last_name': 'Buju',
        'company': first_employer.name
    }
    template = get_template('email/email_template.html')  # email/ pt ca e in templates in directorul email/
    content = template.render(context)  # se ia context si se randeaza in tamplate u nostru
    mail = EmailMultiAlternatives(
        subject='primu meu email trimis din python',
        body=content,
        to=['flavia.buju610@gmail.com']  # 'horvatkarina01@gmail.com',
    )
    mail.content_subtype = 'html'  # pt ca mailu e html
    mail.send()
    return redirect(reverse('home'))  # gen la homepage_view da i am dat name sa mi fie mai usor home in urls


def register_view(request):
    if request.method == "GET":  # pt ca e get tre sa il importam din hr.forms
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect(reverse("home"))

    return render(request, "register.html", {
        'form': form  # trimiti formu form
    })


class RegisterViewSet(viewsets.ViewSet):
    @staticmethod
    def create(request):
        register_serializer = RegisterSerializer(data=request.POST)
        if register_serializer.is_valid():
            register_serializer.create(register_serializer.validated_data)

            content = {
                'message': 'User was created successfully'
            }
            return Response(content, status=200)  # daca nu o mers da eroare 200

        return Response(register_serializer.errors, status=400)  # daca nu intran if da eroare  400

    #  http status codes acolo vezi ce cod 200/400/404 corespunde la ce eroare

    @staticmethod
    def list(request):
        all_users = AuthUserModel.objects.all()
        register_serializer = RegisterSerializer(all_users, many=True) # many=true all users o sa ti dea in postman toti userii

        content = {
            'users': register_serializer.data
        }
        return Response(content, status=200)  # daca nu o mers da eroare 200
