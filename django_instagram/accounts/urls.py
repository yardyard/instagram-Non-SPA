from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),

    # /accounts/login/ => settings.LOGIN_URL에 문자열로 지정되어 있음
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('edit/', views.profile_edit, name='profile_edit'),

    path("password_change/", views.password_change, name="password_change"),
        
    
    ]
