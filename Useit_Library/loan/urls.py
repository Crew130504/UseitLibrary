from django.urls import path
from .views import LoanCreateView, LoanReturnView, LoanHistoryView

urlpatterns = [
    path('create/', LoanCreateView.as_view(), name='loan-create'),
    path('<int:pk>/return/', LoanReturnView.as_view(), name='loan-return'),
    path('my-loans/', LoanHistoryView.as_view(), name='loan-history'),
]
