from knox.auth import AuthToken
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from . import models
from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def get_routes(request):
    try:
        routes = {
            "api/login",
            "api/user",
        }
        return Response(routes)
    except KeyError:
        return Response({
            "details": "error"
        })


@api_view(['GET'])
def get_all_users(request):
    try:
        users = models.User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    except KeyError:
        return Response({
            "details": "error"
        })


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
        })


@api_view(['POST'])
def login_user(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        _, token = AuthToken.objects.create(user)
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
        })
