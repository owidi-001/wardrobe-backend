from django.db import models

from accounts.models import User


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rating = models.IntegerField(default=0)


class Shop(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    logo = models.ImageField(default=None)
    location = models.CharField(max_length=255, default=None)
