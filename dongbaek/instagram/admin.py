from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment

@admin.register(Post) 
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'author', 'message','message_length', 'created_at','updated_at', 'is_public']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public'] # created_at 필드값으로만 필터링 옵션 제공
    #search_fields = ['message'] #message 필드 안에서만 search 함

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 75px;" />')
        return None

    def message_length(self, post): # 매개변수를 주면 안됌
        return f"{len(post.message)} 글자"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
