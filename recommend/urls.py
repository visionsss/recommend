from django.urls import path
from . import views


urlpatterns = [
    path('re_profession/', views.re_profession, name='re_profession'),
    path('re_school/', views.re_school, name='re_school'),
    ]