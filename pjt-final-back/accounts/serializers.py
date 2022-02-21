from rest_framework import serializers
from django.contrib.auth import get_user_model 
from community.serializers import CommunitySerializer, CommentSerializer
from movies.serializers import ReviewDetailSerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    review_set = ReviewDetailSerializer(read_only=True, many=True)
    community_set = CommunitySerializer(read_only=True, many=True)
    comment_set = CommentSerializer(read_only=True, many=True)
    
    class followersSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'profile_img')
    followers = followersSerializer(read_only=True, many=True)
    followings = followersSerializer(read_only=True, many=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'followings', 'profile_img', 'like_genres',
         'review_set', 'community_set', 'comment_set', 'followers', 'id')