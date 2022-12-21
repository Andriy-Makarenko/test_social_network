from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    post = models.TextField(blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    creation_date = models.DateField(auto_now_add=True)

    @property
    def like_count(self):
        return self.likes.filter(like="+").count()

    @property
    def unlike_count(self):
        return self.likes.filter(like="-").count()

    def __str__(self):
        return f"{self.id}-{self.post}"


class PostLike(models.Model):
    LIKE_CHOICES = [
        ("+", "Like"),
        ("-", "Unlike")
    ]
    like = models.CharField(max_length=1, choices=LIKE_CHOICES, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="post_likes")
    post_like = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        unique_together = ("user", "post_like")
