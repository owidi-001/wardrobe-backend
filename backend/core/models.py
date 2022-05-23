from django.db import models

from vendor.models import Vendor

from customer.models import Customer


class Category(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(default=None, blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=150)
    manufacturer = models.CharField(default='generic',max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(default=None, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    message = models.TextField()
