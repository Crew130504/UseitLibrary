from django.urls import path
<<<<<<< HEAD
from .views import RegisterView, CustomTokenObtainPairView, login_view, register_view,current_user_view
=======
from .views import RegisterView, CustomTokenObtainPairView, login_view, register_view
>>>>>>> front

urlpatterns = [
    path('login/', login_view, name='login'),                         
    path('register/', register_view, name='register'),                
<<<<<<< HEAD
    path('registerAPI/', RegisterView.as_view(), name='user-register'),  
    path('loginAPI/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/', current_user_view, name='user-profile'),

=======
    path('api/register/', RegisterView.as_view(), name='user-register'),  
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
>>>>>>> front
]
