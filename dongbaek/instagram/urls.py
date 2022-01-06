from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),
    # 숫자 타입이 나오고, /로 끝날경우 뒤 함수를 호출하겠다는 의미
]