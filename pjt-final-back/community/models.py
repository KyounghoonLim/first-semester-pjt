from django.db import models
from django.conf import settings

def thumbnail_image_path(instance, filename):
    ## MEDIA_ROOT/user_pk/filename 경로로 업로드 
    return f'user_{instance.user.pk}/{filename}'

class Community(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)            
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_community', blank=True) 
    thumbnail = models.ImageField(blank=True, upload_to=thumbnail_image_path)

    def __str__(self):
        return self.title 


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)           
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comment', blank=True)    
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content