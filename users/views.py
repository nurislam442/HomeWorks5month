from django.shortcuts import render
from .models import *
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserRegisterSerializer, UserAuthSerializer, SMSCodeSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import random
from rest_framework.views import APIView
@api_view(['POST'])
def register_api_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    username = serializer.validated_data['username']
    password = serializer.validated_data['password']
    user = User.objects.create_user(username=username, password=password, is_active=False)


    VerificationCode.objects.create(user=user)
    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id': user.id})
    
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
class SMSCodeConfirm(APIView):
    def post(self, request):
        serializer = SMSCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sms_code = serializer.validated_data['sms_code']
        try:
            sms = models.SMSCode.objects.get(sms_code=sms_code)
        except models.SMSCode.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Invalid code'})
        sms.user.is_active = True
        sms.user.save()
        sms.delete()
        return Response(status=status.HTTP_200_OK)