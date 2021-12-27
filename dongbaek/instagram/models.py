from django.contrib.admin.decorators import register
from django.core.checks import messages
from django.db import models

# Create your models here.

class Post(models.Model):
    message = models.TextField(blank=False)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    # Java의 toString과 같은 역할
    def __str__(self):
        return self.message
    """
    def message_length(self): # 매개변수를 주면 안됌
        return len(self.message)
    message_length.short_description = "메세지 글자 수"
    """
