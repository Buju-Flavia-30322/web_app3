from django import forms  # important de importat la formulare
from .utils import store_uploaded_file

# ca sa poti valida parole din baza de date
from django.contrib.auth.password_validation import password_validators_help_text_html
from django.contrib.auth.password_validation import validate_password

from django.contrib.auth import get_user_model

AuthUser = get_user_model()


class UserImageForm(forms.Form):
    image = forms.ImageField(label="Image to upload", required=True)

    def save(self):
        image = self.cleaned_data.get('image')
        store_uploaded_file(image)


# class RegisterForm(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=255, required=True)
#     last_name = forms.CharField(label="Last Name", max_length=255, required=True)
#     email = forms.EmailField(label="Email adress", required=True)
#     password = forms.CharField(
#         label="Password",
#         widget=forms.PasswordInput,
#         required=True,
#         help_text=password_validators_help_text_html
#     )
#     password_confiramation = forms.CharField(
#         label="Password Confirmation",
#         widget=forms.PasswordInput,
#         required=True,
#         help_text="Please confirm your password"
#     )
#
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         try:
#             AuthUser.objects.get(email=email)  # incerci sa cauti user cu emailu ala
#         except AuthUser.DoesNotExist:
#             return email
#         else:
#             raise forms.ValidationError('Email is already taken/used!')
#
#     def clean_password(self):  # setare parola
#         email = self.cleaned_data['email']
#         first_name = self.cleaned_data['first_name']
#         last_name = self.cleaned_data['last_name']
#         password = self.cleaned_data['password']
#
#         user = AuthUser(
#             first_name=first_name,
#             last_name=last_name,
#             email=email
#         )
#         validate_password(password, user)  # daaca parola pt useru ala e ok
#         return password
#
#     def clean_password_confirmation(self):  # confirmare parola
#         password = self.cleaned_data['password']
#         password_confirmation = self.cleaned_data['password_confirmation']
#
#         if password != password_confirmation:
#             raise forms.ValidationError("password not confirmed")
#         return password_confirmation
#
#     def save(self):  # metoda de salvare user prin formu ala
#         first_name = self.cleaned_data['first_name']
#         last_name = self.cleaned_data['last_name']
#         email = self.cleaned_data['email']
#         password = self.cleaned_data['password']
#
#         user = AuthUser.objects.create_user(
#             username=email,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             password=password
#         )
#         return user

class RegisterForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email', 'password']  # 'username',

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=True,
        help_text=password_validators_help_text_html()
    )

    password_confirmation = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput,
        required=True,
        help_text="Please confirm your password"
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match. Please confirm your password.")

        return cleaned_data

    def save(self, commit=True):
        password = self.cleaned_data['password']
        self.instance.set_password(password)

        return super().save(commit)
