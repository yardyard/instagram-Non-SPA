from . import views
from django.urls import path

urlpatterns = [
    path('', views.Post_list, name='post_list'),

]