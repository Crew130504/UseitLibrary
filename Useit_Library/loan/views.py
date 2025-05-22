from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from django.utils.timezone import now
from .models import Loan
from .serializers import LoanSerializer

class LoanCreateView(generics.CreateAPIView):
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        book = serializer.validated_data['book']

        if book.stock < 1:
            raise ValidationError(f"No stock available for book: {book.title}")

        if Loan.objects.filter(user=user, book=book, return_date__isnull=True).exists():
            raise ValidationError("You already have an active loan for this book.")
        
        book.stock -= 1
        book.save()
        serializer.save(user=user)

class LoanReturnView(generics.UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        loan = self.get_object()
        if loan.return_date:
            raise ValidationError("This loan has already been returned.")
        serializer.save(return_date=now())
        book = loan.book
        book.stock += 1
        book.save()

class LoanHistoryView(generics.ListAPIView):
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Loan.objects.filter(user=self.request.user)
