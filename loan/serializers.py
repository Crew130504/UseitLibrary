from rest_framework import serializers
from loan.models import Loan
from book.models import Book
from book.serializers import BookSimpleSerializer

class LoanSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), write_only=True)
    book_details = BookSimpleSerializer(source='book', read_only=True)

    class Meta:
        model = Loan
        fields = ['id', 'user', 'book', 'book_details', 'loan_date', 'return_date']

    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        return super().update(instance, validated_data)
