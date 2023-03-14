from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category, Product, Orders


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_image",
            "get_thumbnail"
        )


class CategoryProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "products",
        )


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "category",
            "name",
            "description",
            "price"
        )


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = (
            "username_id",
            "table",
            "product_name",
            "quantity"
        )


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class OrdersListSerializer(serializers.ModelSerializer):
    username_id = UserInfoSerializer()

    class Meta:
        model = Orders
        fields = "__all__"
