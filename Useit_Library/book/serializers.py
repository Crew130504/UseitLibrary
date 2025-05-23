from rest_framework import serializers
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year', 'stock']
class BookSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']
        
