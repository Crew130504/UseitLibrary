from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.utils.timezone import now
from .models import Loan
from .serializers import LoanSerializer
from user.permissions import IsRegularUser

class LoanCreateView(generics.CreateAPIView):
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated, IsRegularUser]

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
    permission_classes = [permissions.IsAuthenticated, IsRegularUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.return_date:
            raise ValidationError("This loan has already been returned.")

        serializer = self.get_serializer(instance, data={'return_date': now()}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        book = instance.book
        book.stock += 1
        book.save()

        return Response(serializer.data)

class LoanHistoryView(generics.ListAPIView):
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated, IsRegularUser]

    def get_queryset(self):
        return Loan.objects.filter(user=self.request.user)
