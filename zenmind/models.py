from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # item owner
    content = models.TextField() #url of item
    date_posted = models.DateTimeField(default=timezone.now) # date and time of item
    url = models.URLField(blank=True)
    category = models.CharField(max_length=255)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

