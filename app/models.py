from django.conf import settings
from django.db import models
from django.utils import timezone

from collections import defaultdict


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course/', blank=True, null=True)
    description = models.TextField()
    link = models.CharField(max_length=200, default='-')  # !
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    count_test = models.IntegerField(default=0)
    count_ok = models.IntegerField(default=0)
    count_total = models.IntegerField(default=0)
    que_id = defaultdict(int)
    count_corr = defaultdict(int)

    def __str__(self):
        return self.user.username
