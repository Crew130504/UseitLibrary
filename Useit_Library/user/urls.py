from django.urls import path
from .views import RegisterView
from user.views import CustomTokenObtainPairView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

]
