from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    buid = models.PositiveIntegerField(unique=True)
    img = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return self.user.username


class Event(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField()
    img = models.ImageField(upload_to='event_images/')
    location = models.CharField(max_length=255)
    date = models.DateTimeField()

    def __str__(self):
        return f"Event by {self.created_by.user.username} on {self.date}"

