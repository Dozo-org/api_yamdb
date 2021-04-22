from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView


User = get_user_model()


class CreateUser(APIView):
    '''
    Создание пользователя через передачу email в POST запросе
    '''
    def post(self, request):
        confirmation_code = get_random_string(length=12)
        user = User.objects.create(
            email=request.data.get('email'),
            confirmation_code=confirmation_code
        )
        user.save()
        return Response(status=status.HTTP_201_CREATED)


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
            token = RefreshToken.for_user(user)
            return Response(
                {'token': f'{token}'},
                status=status.HTTP_200_OK
            )


