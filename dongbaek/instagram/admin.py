from django.contrib import admin
from .models import Post

@admin.register(Post) 
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','message','message_length', 'created_at','updated_at', 'is_public']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public'] # created_at 필드값으로만 필터링 옵션 제공
    #search_fields = ['message'] #message 필드 안에서만 search 함

    def message_length(self, post): # 매개변수를 주면 안됌
        return len(post.message)
    message_length.short_description = "메세지 글자 수"