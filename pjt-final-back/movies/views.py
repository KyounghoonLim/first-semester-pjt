from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.serializers import ModelSerializer
from .models import Movie, Genre, Review
from rest_framework.response import Response
from rest_framework.views import status
from .serializers import MovieSerializer, ReviewSerializer, GenreSerializer
from django.contrib.auth import get_user
from accounts.models import User
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from accounts.views import getUser
# from django.db.models import Q
# Create your views here.

def movie_recommand(user, page):
    if page == 0:
        user_like_genres = user.like_genres.all().values()
        recommanded_movies = []
        for gen in user_like_genres:
            genre = get_object_or_404(Genre, pk=gen['id'])
            recommanded_movies.extend(genre.movie_set.order_by('-vote_average'))
            # filtered_movies.extend(Movie.objects.filter(genres=gen['id']).values())
        # recommanded_movies = list({ each['id'] : each for each in filtered_movies }.values()) # 중복 제거 코드
        # recommanded_movies.sort(key=lambda x: x['vote_average'], reverse=True)
    elif page == 1:
        recommanded_movies = list(Movie.objects.order_by('-release_date'))
    elif page == 2:
        recommanded_movies = list(Movie.objects.order_by('vote_average'))
    else:
        recommanded_movies = list(Movie.objects.order_by('-vote_average'))
        return recommanded_movies[:40]

    return recommanded_movies[:20]


@api_view(['GET'])
def index(request):
    page = int(request.GET.get('page'))
    recommanded_movies = movie_recommand(getUser(request), page)
    serializer = MovieSerializer(recommanded_movies, many=True)

    return Response(serializer.data)

    return JsonResponse(recommanded_movies, safe=False)


@api_view(['GET'])
def get_genres(requset):
    genres = get_list_or_404(Genre)
    genre_serializer = GenreSerializer(genres, many=True)

    return Response(genre_serializer.data)


@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie_serializer = MovieSerializer(movie)

    return Response(movie_serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST'])
def review(request, movie_pk):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)

        review_serializer = ReviewSerializer(data=request.data)
        if review_serializer.is_valid(raise_exception=True):
            if review_serializer.validated_data['score'] > 10:
                review_serializer.validated_data['score'] = 10
            review_serializer.save(movie=movie, user=request.user)
            votes = len(Review.objects.filter(movie=movie))
            if votes > 2:
                movie.vote_average = round((movie.vote_average * votes + review_serializer.data['score']) / (votes + 1), 2)
            else:
                movie.vote_average = round((movie.vote_average + review_serializer.data['score']) / (votes + 1), 2)
            movie.save()
            movie_serializer = MovieSerializer(movie)
            return Response(movie_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT' and request.user.review_set.filter(pk=review_pk).exists():
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE' and request.user.review_set.filter(pk=review_pk).exists():
        review.delete()
        context = {
            'delete': f'{review_pk}번 댓글이 삭제되었습니다'
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'detail': '권한이 없습니다'}, status=status.HTTP_403_FORBIDDEN)

        