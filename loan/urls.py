from django.urls import path
from .views import LoanCreateView, LoanReturnView, LoanHistoryView,loan_template

urlpatterns = [
    path('loan_template/', loan_template, name='loan-frontend'),

    path('create/', LoanCreateView.as_view(), name='loan-create'),
    path('return/<int:pk>/', LoanReturnView.as_view(), name='loan-return'),
    path('history/', LoanHistoryView.as_view(), name='loan-history'),
]
