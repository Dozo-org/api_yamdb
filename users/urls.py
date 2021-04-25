from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CreateUser, MyTokenObtainPairView, UserViewMe, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='UserView')

urlpatterns = [
     path('v1/auth/email/',
          CreateUser.as_view(),
          name='user_creat'),
     path('v1/auth/token/',
          MyTokenObtainPairView.as_view(),
          name='token_obtain_pair'),
     path('v1/users/me/',
          UserViewMe.as_view(),
          name='user_me'),
     path('v1/', include(router.urls)),
]
