#models.py
from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
        # return self.title

class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"Booking for {self.name} on {self.booking_date}"
class User(models.Model):
    url = models.URLField()
    username = models.CharField(max_length=255)
    email = models.EmailField()
    group = models.CharField(max_length=255)

    def __str__(self):
        return self.username