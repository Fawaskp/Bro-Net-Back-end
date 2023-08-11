from django.db import models
from accounts.models import User


class Banner(models.Model):
    heading = models.CharField(max_length=60)
    content = models.CharField(max_length=250)


class Post(models.Model):
    TYPE_CHOICES = (
        ("image", "Image"),
        ("video", "Video"),
        ("poll", "Poll"),
        ("article", "Article"),
    )

    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    type           = models.CharField(max_length=10, choices=TYPE_CHOICES)
    created_at     = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at     = models.DateTimeField(auto_now=True, blank=True)
    description    = models.TextField()
    like_count     = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)

class ImagePost(models.Model):
    post  = models.ForeignKey(Post,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image-post') 
    class Meta:
        ordering = ['-id']


class VideoPost(models.Model):
    post  = models.ForeignKey(Post,on_delete=models.CASCADE)
    video = models.FileField(upload_to='post-video')

class ArticlePost(models.Model):
    post    = models.ForeignKey(Post,on_delete=models.CASCADE)
    heading = models.CharField(max_length=50)
    body    = models.TextField()


