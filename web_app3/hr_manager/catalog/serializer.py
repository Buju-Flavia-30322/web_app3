from rest_framework import serializers
from .models import Category
from .models import Product
from .models import ProductCategory


class CategorySerializer(serializers.ModelSerializer):  # la proiect serializezi tote
    class Meta:
        model = Category
        exclude = []


class ProductCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = ProductCategory
        exclude = []


class ProductSerializer(serializers.ModelSerializer):
    categories = ProductCategorySerializer(many=True, source='categories_pivot')

    class Meta:
        model = Product
        exclude = []
        depth = 1 # aduce date din mai multe serializere si tre sa aiba depth 1 sa fie ok
