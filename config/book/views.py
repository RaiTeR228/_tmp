from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics
from .models import Book
from config.serializers import BookSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save()

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class add_book_view(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

