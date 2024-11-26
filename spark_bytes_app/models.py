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
    food_items = models.TextField(blank=True, null=True, help_text="List of food items available at the event")
    food_types = models.CharField(
        max_length=255, blank=True, null=True, help_text="Types of food available (e.g., vegetarian, vegan, non-veg)"
    )
    allergies = models.TextField(blank=True, null=True, help_text="List of common allergens to be aware of")
    reserved_by = models.ManyToManyField(Profile, related_name='reserved_events', blank=True)

    def __str__(self):
        return f"Event: {self.name} by {self.created_by.user.username}"

