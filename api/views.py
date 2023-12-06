from django.contrib.auth import get_user_model
from knox.auth import AuthToken, TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models
from .serializers import UserSerializer, StudentSerializer


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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_user(request):
    try:
        return Response({
            "details": "Token is valid"
        }, status=status.HTTP_200_OK)
    except KeyError:
        return Response({
            "details": "Token is invalid"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_student(request):
    try:
        user = request.user
        student = models.Student.objects.get(username=user.username)

        if student is not None:
            serializer = StudentSerializer(student)
            return Response(serializer.data)

    except KeyError:
        return Response({
            "details": "error"
        }, status=status.HTTP_400_BAD_REQUEST)
    except models.Student.DoesNotExist:
        return Response({
            "details": "Student not found"
        }, status=status.HTTP_404_NOT_FOUND)
