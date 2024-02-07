from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password # ca sa hasurezi parole in db
AuthUserModel = get_user_model()


# datele de aici tre sa fie la fel ca users/models.py
class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)

    # validari, nu le am mai implementat dar undeva le ai in models/users exemplu
    @staticmethod
    def validate_email(email):
        return email

    @staticmethod
    def validate_password(password):
        return password

    def create(self, validated_data):
        AuthUserModel.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=make_password()['password'],  # ca sa nu se vada in baza de date parola tre sa ii pui hash sau cv gen make_password
        )

    def update(self, instance, validated_data):
        pass

