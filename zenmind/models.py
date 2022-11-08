from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    item_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #item owner
    item_url = models.TextField() #url of item
    created_date = models.DateTimeField(default=timezone.now) #date and time of item
    flag = models.CharField(max_length=200) #main flag for item


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.flag
    