from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from . import models
from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def get_routes(request):
    routes = {
        "api/login",
        "api/user",
    }
    return Response(routes)


@api_view(['GET'])
def get_all_users(request):
    users = models.User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    try:
        username = request.data["username"]
        user = User.objects.filter(username=username).first()

        # check email already exist or not
        if user is not None:
            return Response({
                "username": "This username already registered"
            })

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "details": "success"
        })
    except KeyError:
        return Response({
            "details": "error"
        })


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
