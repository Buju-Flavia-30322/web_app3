from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated  # ca sa nu poti sa get post etc produse fara sa fi autentificat


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,) # tuple cu diverse permisiuni

    def get_queryset(self):
        return Product.objects.all()
