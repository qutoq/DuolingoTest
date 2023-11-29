from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.main, name="main"),
    path("post", views.post_list, name="post"),
    path("post/new", views.post_new, name="new post"),
    path('register', views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
