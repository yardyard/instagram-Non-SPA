from . import views
from django.urls import path

app_name = 'inflearn' # URL Reverse에서 namespace 역할을 하게 된다.


urlpatterns = [
    path('', views.Post_list, name='post_list'),

]