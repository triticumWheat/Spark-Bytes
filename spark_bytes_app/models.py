from django.db import models
from django.contrib.auth.models import User


# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    buid = models.CharField(max_length=8)
    img = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'


from django.db import models

class Event(models.Model):
    # Define choices for food types and allergies (same as your existing code)
    FOOD_TYPES = [
        ('Italian', 'Italian'),
        ('Mediterranean', 'Mediterranean'),
        ('Salad', 'Salad'),
        ('American', 'American'),
        ('BBQ', 'BBQ'),
        ('Chinese', 'Chinese'),
        ('Korean', 'Korean'),
        ('Japanese', 'Japanese'),
        ('Mexican', 'Mexican'),
        ('Spanish', 'Spanish'),
        ('Indian', 'Indian'),
        ('Thai', 'Thai'),
        ('Vietnamese', 'Vietnamese'),
        ('Sushi', 'Sushi'),
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Vegan', 'Vegan'),
        ('Vegetarian', 'Vegetarian'),
    ]

    ALLERGIES = [
        ('Dairy', 'Dairy'),
        ('Soy', 'Soy'),
        ('Nuts', 'Nuts'),
        ('Fish', 'Fish'),
        ('Shellfish', 'Shellfish'),
        ('Eggs', 'Eggs'),
        ('Wheat', 'Wheat'),
        ('Sesame', 'Sesame'),
    ]
    
    # Fields for the Event model
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey('Profile', on_delete=models.CASCADE)
    description = models.TextField()
    img = models.ImageField(upload_to='event_images/')
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    food_items = models.TextField(blank=True, null=True, help_text="List of food items available at the event")
    food_types = models.CharField(
        max_length=50, choices=FOOD_TYPES, blank=True, null=True, help_text="Select the type of food available."
    )
    allergies = models.CharField(
        max_length=50, choices=ALLERGIES, blank=True, null=True, help_text="Select common allergens to be aware of."
    )
    reserved_by = models.ManyToManyField('Profile', related_name='reserved_events', blank=True)
    reservation_limit = models.PositiveIntegerField(default=50, help_text="Maximum number of reservations for this event")
    


    # Other fields...
    latitude = models.FloatField(blank=True, null=True)  # Remove max_digits and decimal_places
    longitude = models.FloatField(blank=True, null=True)  # Remove max_digits and decimal_places

    # Other methods...



    def is_full(self):
        """Check if the event has reached its reservation limit."""
        return self.reserved_by.count() >= self.reservation_limit

    def __str__(self):
        return f"Event: {self.name} by {self.created_by.user.username}"
