from rest_framework import serializers

from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'price', 'genre', 'author', 'year_published', 'id']
        read_only_fields = ['id']


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'country', 'region', 'city', 'street', 'house', 'books', 'id']
        read_only_fields = ['id']


class BookSoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSold
        fields = ['book', 'purchase', 'quantity', 'id']
        read_only_fields = ['id']


class InStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = InStock
        fields = ['shop', 'book', 'quantity', 'id']
        read_only_fields = ['id']


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['client', 'shop', 'book', 'full_price', 'id']
        read_only_fields = ['id']


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['user', 'id']
