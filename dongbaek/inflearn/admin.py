from django.contrib import admin
from .models import Post
# Register your models here.

# Post 클래스 상속받음
admin.site.register(Post)
