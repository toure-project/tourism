from django.db import models

class Events(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_image')
    description = models.TextField(max_length=200)
    date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "events"