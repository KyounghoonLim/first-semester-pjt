from django.db import models
from rest_framework import serializers 
from .models import Movie, Genre, Review
from django.contrib.auth import get_user_model

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Review
        fields = ('content', 'score')


class ReviewDetailSerializer(serializers.ModelSerializer):

    class ReviewMovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('title',)

    movie = ReviewMovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    
    class MovieReviewSerializer(serializers.ModelSerializer):

        class ReviewUserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('username', 'id', 'profile_img')
        user = ReviewUserSerializer(read_only=True)
        
        class Meta:
            model = Review
            fields = ('content', 'user', 'score', 'id')

    review_set = MovieReviewSerializer(read_only=True, many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'vote_average', 'genres',
            'poster_path', 'release_date', 'review_set', 'id')


