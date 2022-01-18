from . import views
from django.urls import path, re_path, register_converter
from .converters import YearConverter, MonthConverter, DayConverter

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'Month')
register_converter(DayConverter, 'Day')

app_name = 'instagram' # URL Reverse에서 namespace 역할을 하게 된다.

urlpatterns = [ 
    path('new/', views.post_new, name='post_new'),
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'), # Post.DoesNotExist 오류
    # 숫자 타입이 나오고, /로 끝날경우 뒤 함수를 호출하겠다는의미
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    #path('archive/<year:year>/<month:month>/', views.post_archive_month, name='post_archive_month'),
    #path('archive/<year:year>/<month:month>/<day:day>/', views.post_archive_day, name='post_archive_day'),

]