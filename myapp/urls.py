from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path("", views.home, name="home"),
    path("films", views.films, name = "films"),
    path('api/movie_titles/', views.movie_titles, name='movie_titles'),
    path("register", views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name="user-logout")
]
