from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.utils import timezone

from .forms import UserRegistrationForm, ContactForm
from .models import Profile, Course


def main(request):
    courses = Course.objects.all()
    status = "norm"
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.timeAdd = timezone.now()
            msg.save()
            form = ContactForm()
            status = "ok"
        else:
            status = "fail"
    else:
        form = ContactForm()
    return render(request, "DuolingoTest.html", {"form": form, "courses": courses, "status": status})


# registration


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

    return render(request, 'registration/registration.html', {"form": form})


@login_required(login_url='app:login')
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
    else:
        form = PasswordChangeForm(user)
    return render(request, 'registration/password_change.html', {'form': form})


@login_required(login_url='app:login')
def profile(request):
    username = request.user.username
    user = get_user_model().objects.filter(username=username).first()
    return render(request, 'profile.html', {"user": user})



