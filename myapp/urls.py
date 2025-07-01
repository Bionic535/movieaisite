from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("films", views.films, name = "films"),
    path('api/movie_titles/', views.movie_titles, name='movie_titles'),
    path("register/", views.RegisterView, name="register"),
    path("login/", views.LoginView, name="login"),
]
