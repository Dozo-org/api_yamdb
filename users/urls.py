from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import AccessToken, CreateUser, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='UserView')

urlpatterns = [
    path('v1/auth/email/',
         CreateUser.as_view(),
         name='user_creat'),
    path('v1/auth/token/',
         AccessToken.as_view(),
         name='token_obtain_pair'),
    path('v1/', include(router.urls)),
]
