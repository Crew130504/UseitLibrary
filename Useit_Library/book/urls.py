from django.urls import path
from book.views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, book_list_template,book_detail_template

urlpatterns = [
    path('', book_list_template, name='book-home'), 
    path('books/<int:id>/', book_detail_template, name='book-detail'),


    path('api/books/data/', BookListView.as_view(), name='book-list'),
    path('api/books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('api/books/create/', BookCreateView.as_view(), name='book-create'),
    path('api/books/<int:id>/update/', BookUpdateView.as_view(), name='book-update'),
    path('api/books/<int:id>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
