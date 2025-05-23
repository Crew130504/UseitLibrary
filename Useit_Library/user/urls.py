from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, login_view, register_view

urlpatterns = [
    path('login/', login_view, name='login'),                         
    path('register/', register_view, name='register'),                
    path('api/register/', RegisterView.as_view(), name='user-register'),  
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
