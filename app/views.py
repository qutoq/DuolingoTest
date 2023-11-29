from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.utils import timezone

from .forms import UserRegistrationForm
from .models import Post, Profile, Course


def main(request):
    courses = Course.objects.all()
    return render(request, "html/main.html", {'courses': courses})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'html/post.html', {'posts': posts})


def post_new(request):
    pass


def register(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Profile.objects.create(user=user)
            return redirect('/')
    else:
        form = UserRegistrationForm()

    return render(request, 'html/registration.html', {"form": form})
