from django.db import models
from django.utils import timezone

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    feedback_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    




class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    #image = models.ImageField(upload_to='event_images/')
    expiration_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=1))

    def __str__(self):
        return self.name

