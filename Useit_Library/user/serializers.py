from rest_framework import serializers
from user.models import User
from loan.models import Loan

class UserSerializer(serializers.ModelSerializer):
    borrowed_books = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'role', 'borrowed_books']

    def get_borrowed_books(self, obj):
        loans = Loan.objects.filter(user=obj)
        return [loan.book.title for loan in loans]
