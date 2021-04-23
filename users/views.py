from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from rest_framework import viewsets, filters, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, Token
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from .serializer import UserSerializer
from .permission import IsAdmin


User = get_user_model()


class CreateUser(APIView):
    '''
    Создание пользователя через передачу email в POST запросе
    '''
    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')
        confirmation_code = get_random_string(length=12)
        if username is None:
            username = email.split('@')[0]
        user = User.objects.create(
            email=email,
            username=username,
            confirmation_code=confirmation_code
        )
        user.save()
        return Response(username, status=status.HTTP_201_CREATED)


class AccessToken(APIView):
    '''
    Получение токена
    '''
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response(
                data={'error': 'Не передан email'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {'error': 'Пользователя с таким email не существует'},
                status=status.HTTP_400_BAD_REQUEST
            )
        confirmation_code = request.data.get('confirmation_code')
        if confirmation_code == user.confirmation_code:
            #token = RefreshToken.for_user(user)
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            )
            #return {
                #'refresh': str(refresh),
                #'access': str(refresh.access_token),
            #}
            #return Response(
                #{'token': f'{token}'},
                #status=status.HTTP_200_OK
            #)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', ]

