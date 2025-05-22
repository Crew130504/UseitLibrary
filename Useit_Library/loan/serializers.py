from rest_framework import serializers
from loan.models import Loan

class LoanSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    book = serializers.StringRelatedField()

    class Meta:
        model = Loan
        fields = ['id', 'user', 'book', 'loan_date', 'return_date']
