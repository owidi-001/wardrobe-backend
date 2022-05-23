from django.db import models

from accounts.models import User


class Location(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
