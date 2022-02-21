from django.contrib import auth
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Comment, Community
from .serializers import CommentSerializer, CommunitySerializer, CommunityDetailSerializer, CommentDetailSerializer
from django.contrib.auth import get_user, get_user_model
import base64
from django.conf import settings
# Create your views here.

@api_view(['GET', 'POST'])
def community(request):
    if request.method == 'GET':
        communities = Community.objects.all()
        serializer = CommunityDetailSerializer(communities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def community_detail(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)

    if request.method == 'GET':
        serializer = CommunityDetailSerializer(community)
       
        return Response(serializer.data)
    
    elif request.method == 'PUT' and request.user.community_set.filter(pk=community_pk).exists():
        serializer = CommunitySerializer(community, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE' and request.user.community_set.filter(pk=community_pk).exists():
        community.delete()
        context = {
            'delete': f'{community_pk}번 게시글이 삭제되었습니다'
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)

    else:
        return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)



@api_view(['POST'])
def community_like(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    user = request.user 

    if community.like_users.filter(pk=user.pk).exists():
        community.like_users.remove(user)
        
    else:
        community.like_users.add(user)
    serializer = CommunityDetailSerializer(community)
    
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def comment(request, community_pk):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentDetailSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        community = get_object_or_404(Community, pk=community_pk)
        _serializer = CommentSerializer(data=request.data)
        print('before')
        if _serializer.is_valid(raise_exception=True):
            _serializer.save(community=community, user=request.user)

            serializer = CommunityDetailSerializer(community)

            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, community_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentDetailSerializer(comment)
        author = get_object_or_404(get_user_model(), pk=serializer['user'].value).username
        result = dict(serializer.data)
        result['author'] = author
        return Response(result)
    
    elif request.method == 'PUT' and request.user.comment_set.filter(pk=comment_pk).exists():
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE' and request.user.comment_set.filter(pk=comment_pk).exists():
        comment.delete()
        context = {
            'delete': f'{comment_pk}번 댓글이 삭제되었습니다'
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)
    
    else:
        return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def comment_like(request, community_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = request.user 

    if comment.like_users.filter(pk=user.pk).exists():
        comment.like_users.remove(user)
        like = False 
    else:
        comment.like_users.add(user)
        like = True 
    
    context = {
        'like': like,
        'count_comment_like': comment.like_users.count()
    }
    return Response(context)

