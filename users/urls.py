# from django.urls import include, path
# from rest_framework.routers import DefaultRouter
# from .views import AccessToken, CreateUser, UserViewMe, UserViewSet

# router = DefaultRouter()
# router.register('users', UserViewSet, basename='UserView')

# urlpatterns = [
#      path('v1/auth/email/',
#           CreateUser.as_view(),
#           name='user_creat'),
#      path('v1/auth/token/',
#           AccessToken.as_view(),
#           name='token_obtain_pair'),
#      path('v1/users/me/',
#           UserViewMe.as_view(),
#           name='user_me'),
#      path('v1/', include(router.urls)),
# ]

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AccessToken, CreateUser, UserViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet)

authentication_patterns = [
    path('email/', CreateUser.as_view()),
    path('token/', AccessToken.as_view(), name='token_obtain_pair'),
]

urlpatterns = [
    path('v1/auth/', include(authentication_patterns)),
    path('v1/', include(router.urls)),
]
