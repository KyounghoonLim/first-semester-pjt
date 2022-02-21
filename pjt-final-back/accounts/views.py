from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from movies.models import Movie, Genre
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
import jwt
from rest_framework_jwt.utils import jwt_decode_handler
# Create your views here.

def getUser(request):
    auth_token = request.headers.get('Authorization')[4:]
    payload = jwt_decode_handler(auth_token)
    user = get_object_or_404(get_user_model(), username=payload['username'])

    return user


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):

    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    if password != password_confirmation:
        return Response({'error': '일치하지 않는 비밀번호입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def my_profile(request):
    person = getUser(request)

    if request.method == 'GET':
        serializer = UserSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        temp = set()
        for mov in request.data.get('like_movies'):
            movie = get_object_or_404(Movie, pk=mov)
            for gen in movie.genres.all().values():
                temp.add(gen['id'])
        for gen_pk in temp:
            gen = get_object_or_404(Genre, pk=gen_pk)
            person.like_genres.add(gen)
        serializer = UserSerializer(person)
        
        return Response(serializer.data)


@api_view(['GET'])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    serializer = UserSerializer(person)

    return Response(serializer.data)


@api_view(['POST'])
def follow(request, user_pk):

    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = getUser(request)

    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)

        else:
            person.followers.add(user)

    serializer = UserSerializer(person)

    return JsonResponse(serializer.data)


