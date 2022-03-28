from turtle import title
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('published', 'Published')
    }

    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title
        
class Comment(models.Model):
    user = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.SmallIntegerField(
        choices=[(i, i) for i in range(1, 6)], null=True, blank=True)

    class Meta:
        unique_together = (
            'book',
            'user'
        )

