from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import *
from .permissions import IsOwner, IsSeller
from .serializers import *


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner | IsSeller]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ShopViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class BookSoldViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner | IsSeller | IsAuthenticated]
    queryset = BookSold.objects.all()
    serializer_class = BookSoldSerializer


class InStockViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner | IsSeller]
    queryset = InStock.objects.all()
    serializer_class = InStockSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner | IsSeller | IsAuthenticated]
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class SellerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner]
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class BooksRecentlyPublishedView(generics.ListCreateAPIView):
    permission_classes = [IsOwner]
    queryset = Book.objects.filter(year_published__gt=2019)
    serializer_class = BookSerializer


class BooksByPublicationYearView(generics.ListCreateAPIView):
    permission_classes = [IsOwner]
    serializer_class = BookSerializer

    def get_queryset(self):
        year_published = self.kwargs['year_published']
        return Book.objects.filter(year_published=year_published)
