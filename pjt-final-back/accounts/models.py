from django.db import models
from django.contrib.auth.models import  AbstractUser

from movies.models import Genre

def profile_image_path(instance, filename):
    ## MEDIA_ROOT/user_pk/filename 경로로 업로드 
    return f'user_{instance.pk}/{filename}'

class User(AbstractUser):
    ## followings: user가 팔로우 하는// followers: 유저를!!! 팔로우 하는 
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True) 
    # profile_img = models.ImageField(blank=True, upload_to='images/')             #### upload_to 
    profile_img = models.ImageField(blank=True, upload_to=profile_image_path)
    like_genres = models.ManyToManyField(Genre, blank=True)          


