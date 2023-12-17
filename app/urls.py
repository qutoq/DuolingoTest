from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path("", views.main, name="main"),
    path("post", views.post_list, name="post"),

    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout', ),
    path('logout-then-login', auth_views.logout_then_login, name='logout_then_login'),

    path('register', views.register, name='register'),
    path('password_change', views.password_change, name="password_change"),
    path('profile', views.profile, name='profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = 'app'
