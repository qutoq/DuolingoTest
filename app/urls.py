from django.urls import path
from . import views


urlpatterns = [
    path("", views.main, name="main"),
    path("post", views.post, name="post"),
    path('register', views.register, name='register'),
]
