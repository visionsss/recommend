from django.urls import path
from . import views


urlpatterns = [
    path('', views.mbti, name='mbti'),
    path('test/', views.mbti_test, name='mbti_test')
    ]