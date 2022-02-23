from django.urls import path, re_path
from django.contrib.auth.validators import UnicodeUsernameValidator

from . import views

# reverse에 사용할 이름
app_name = 'insta'

# 주소에 오는 username이 Unicode 형태인지 확인하는 Validator 
# username_regax = UnicodeUsernameValidator.regex.lstrip('^').strip('$')

urlpatterns = [
    path('', views.index, name='index'),

    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/<int:pk>/like/', views.post_like, name='post_like'),
    path('post/<int:pk>/unlike/', views.post_unlike, name='post_unlike'),
    # 아래 path에서는 comment가 주인공이기에 post_pk로 작성
    path('post/<int:post_pk>/comment/new/', views.comment_new, name='comment_new'),

    re_path(r'^(?P<username>[\w.@+-]+)/$', views.user_page, name='user_page'),    
    ]


