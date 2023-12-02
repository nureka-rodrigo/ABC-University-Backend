from django.contrib.auth import get_user_model
from knox.auth import AuthToken
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from . import models
from .serializers import UserSerializer


@api_view(['GET'])
def get_routes(request):
    try:
        routes = {
            "api/login",
            "api/user",
        }
        return Response(routes, status=status.HTTP_200_OK)
    except KeyError:
        return Response({
            "details": "error"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_users(request):
    try:
        users = models.User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except KeyError:
        return Response({
            "details": "error"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_user(request):
    try:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response({
            'user_info': {
                'username': user.username,
                'password': user.password
            },
        }, status=status.HTTP_200_OK)
    except KeyError:
        return Response({
            "details": "error"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        user = get_user_model().objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        _, token = AuthToken.objects.create(user)
        user.is_active = True
        user.save()
        return Response({
            'user_info': {
                'username': user.username,
                'password': user.password
            },
            'token': token
        }, status=status.HTTP_200_OK)
    except KeyError:
        return Response({
            "details": "error"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def check_user(request):
    user = get_user_model().objects.get(username='admin')
    if user.is_active:
        return Response({
            "details": "Authenticated"
        }, status=status.HTTP_200_OK)

    return Response({
        "details": "Not authenticated"
    }, status=status.HTTP_400_BAD_REQUEST)
