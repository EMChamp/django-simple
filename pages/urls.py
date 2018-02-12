# pages/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('news/', views.news_page, name='news_page'),
    path('anime/', views.anime_page, name='anime_page'),
]

