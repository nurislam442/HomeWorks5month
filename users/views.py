from django.shortcuts import render
from .models import *
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer, UserAuthSerializer, UserConfirmSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import random
@api_view(['POST'])
def register_api_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    username = serializer.validated_data['username']
    password = serializer.validated_data['password']
    user = User.objects.create_user(username=username, password=password, is_active=False)

    code = str(random.randint(100000, 999999))

    VerificationCode.objects.create(user=user, code=code)
    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id': user.id, "code": code})
    
@api_view(['POST'])
def auth_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data={'User credentials are wrong!'})

@api_view(["POST"])
def confirm_api_view(request):
    # Десериализуем входные данные
    serializer = UserConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data["username"]
    password = serializer.validated_data["password"]
    code = serializer.validated_data["code"]

    # Пытаемся найти пользователя
    user = User.objects.filter(username=username).first()

    if user:
        # Проверка пароля
        if not user.check_password(password):
            return Response({"detail": "Неверные учетные данные."}, status=status.HTTP_401_UNAUTHORIZED)

        # Получаем код подтверждения для пользователя
        try:
            verification_code = VerificationCode.objects.get(user=user)

            # Проверка на совпадение ключа
            if verification_code.code != code:
                return Response({"detail": "Неверный код подтверждения."}, status=status.HTTP_400_BAD_REQUEST)

            # Если код совпадает, активируем пользователя
            user.is_active = True
            user.save()

            # Удаляем код после успешного подтверждения
            verification_code.delete()

            return Response({"detail": "Аккаунт успешно подтвержден."}, status=status.HTTP_200_OK)

        except VerificationCode.DoesNotExist:
            return Response({"detail": "Код подтверждения не найден."}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"detail": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)
