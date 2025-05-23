from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from user.permissions import IsAdminRole
from django.shortcuts import render

def book_list_template(request):
    return render(request, 'book/index.html')

def book_detail_template(request, id):
    return render(request, 'book/detail.html')

<<<<<<< HEAD
def management_template(request):
    return render(request, 'book/management.html')
=======
>>>>>>> front

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminRole]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated, IsAdminRole]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated, IsAdminRole]
