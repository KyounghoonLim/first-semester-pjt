from rest_framework import serializers 
from .models import Community, Comment 
from django.contrib.auth import get_user_model


class CommunitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Community
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'thumbnail', 'like_users')
        read_only_field = ('user',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment 
        fields = ('content',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'profile_img')


class CommentDetailSerializer(serializers.ModelSerializer):
    community = CommunitySerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment 
        fields = ('content', 'user', 'like_users', 'community',
        'created_at', 'updated_at')


class CommunityDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentDetailSerializer(many=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Community
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',
         'thumbnail', 'like_users', 'user', 'comment_set')