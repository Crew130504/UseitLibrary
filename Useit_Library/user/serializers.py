from rest_framework import serializers
from django.contrib.auth import get_user_model
from loan.models import Loan

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    borrowed_books = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'borrowed_books']

    def get_borrowed_books(self, obj):
        loans = Loan.objects.filter(user=obj)
        return [loan.book.title for loan in loans]
