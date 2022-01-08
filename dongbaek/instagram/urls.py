from . import views
from django.urls import path, re_path, register_converter

class YearConverter:
    regex = r"\d{4}"

    def to_python(self, value): # url로부터 추출한 문자열을 뷰에 넘겨주기 전에 변환
        return int(value)
    
    def to_url(self, value): # url reverse 시에 호출
        return str(value)

register_converter(YearConverter, 'year')

app_name = 'instagram' # URL Reverse에서 namespace 역할을 하게 된다.

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail), # Post.DoesNotExist 오류
    # 숫자 타입이 나오고, /로 끝날경우 뒤 함수를 호출하겠다는 의미
    path('archives/<year:year>/', views.archives_year),
]