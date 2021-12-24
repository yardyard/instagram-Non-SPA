
# 필요한 모듈과 함수를 임포트합니다.
from django.contrib import admin 
from django.urls import path, include
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# from bookmark.views import BookmarkLV, BookmarkDV


# path() 함수는 route, view 2개의 필수 인자와 kwarge, name 2개의 선택 인자를 받습니다. 
urlpatterns = [
    #장고에서는 Admin 사이트에 대한 URLconf는 이미 정의 되어있습니다.
    path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    
    
    
    
    
    
    
    # class-based views
    # URL /bookmark/ 요청을 처리할 뷰 클래스를 BookmarkLV로 지정합니다. 패턴의 이름은 'index'로 지정합니다.
   # path('bookmark/', BookmarkLV.as_view(), name='index'),
    # URL /bookmark/99/ 요청을 처리할 뷰 클래스를 BookmarkDV로 지정합니다. 패턴의 이름은 'detail'로 지정합니다.
    # BookmarkDV 뷰 클래스에 pk=99라는 인자가 전달 됩니다.
  #  path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),

]

