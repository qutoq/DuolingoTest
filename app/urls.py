from django.urls import path
from . import views


urlpatterns = [
    path("", views.main, name="main"),
    path("post", views.post_list, name="post"),
    path("post/new", views.post_new, name="new post"),
    path('register', views.register, name='register'),
]
