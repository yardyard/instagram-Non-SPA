from django.urls import path, re_path
from django.contrib.auth.validators import UnicodeUsernameValidator

from . import views

# reverse에 사용할 이름
app_name = 'insta'

# 주소에 오는 username이 Unicode 형태인지 확인하는 Validator 
# username_regax = UnicodeUsernameValidator.regex.lstrip('^').strip('$')

urlpatterns = [
    
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),


    re_path(r'^(?P<username>[\w.@+-]+)/$', views.user_page, name='user_page'),    
    ]


