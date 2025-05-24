from rest_framework import serializers
from loan.models import Loan
from book.models import Book

class LoanSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    book_title = serializers.SerializerMethodField()
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Loan
        fields = ['id', 'user', 'book', 'book_title', 'loan_date', 'return_date']

    def get_book_title(self, obj):
        return obj.book.title if obj.book else None

    def update(self, instance, validated_data):
        validated_data.pop('book', None)
        validated_data.pop('user', None)
        return super().update(instance, validated_data)
