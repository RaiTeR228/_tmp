from django.contrib import admin
from django.urls import path
from book.views import ProductList, ProductDetail, add_book_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', ProductList.as_view(), name='book-list'),
    path('api/books/<int:pk>/', ProductDetail.as_view(), name='book-detail'),
]