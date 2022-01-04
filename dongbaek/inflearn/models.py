from typing import ContextManager
from django.conf import settings
from django.db import models
from django.conf import settings

from django.db.models.deletion import CASCADE
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name="inflearn_author_set")
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
