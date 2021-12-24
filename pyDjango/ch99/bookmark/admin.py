from django.contrib import admin
from bookmark.models import Bookmark

# Bookadmin 클래스는 Bookmark 클래스가 Admin 사이트에서 어떤 모습으로 보여줄지를 정의하는 클래스입니다.


# @admin.register() 데코레이터를 사용하여 어드민 사이트에 등록합니다.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    
    # Bookmark 내용을 보여줄 때, id와 title, url을 화면에 출력하라고 지정했습니다.
    list_display = ('id', 'title', 'url')

