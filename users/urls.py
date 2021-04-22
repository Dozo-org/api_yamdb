from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import AccessToken, CreateUser

urlpatterns = [
    path('auth/email/',
         CreateUser.as_view(),
         name='user_creat'),
    path('auth/token/',
         AccessToken.as_view(),
         name='token_obtain_pair'),
]
