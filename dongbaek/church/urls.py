from django.urls import path, include
from . import views
from django.views.generic import TemplateView

app_name ='church'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='church'),
]