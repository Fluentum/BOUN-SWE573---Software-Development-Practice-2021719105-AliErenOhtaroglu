from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #item owner
    content = models.TextField() #url of item
    date_posted = models.DateTimeField(default=timezone.now) #date and time of item


    def __str__(self):
        return self.title

"""
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.flag
    
"""
