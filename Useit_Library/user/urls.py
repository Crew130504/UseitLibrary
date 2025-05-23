from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, login_view, register_view,current_user_view

urlpatterns = [
    path('login/', login_view, name='login'),                         
    path('register/', register_view, name='register'),                
    path('registerAPI/', RegisterView.as_view(), name='user-register'),  
    path('loginAPI/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/', current_user_view, name='user-profile'),

]
