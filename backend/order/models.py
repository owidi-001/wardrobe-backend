from django.db import models

from cart.models import Cart


class Order(models.Model):
    STATUS = (
        ('P', 'PENDING'),
        ('A', 'ACTIVE'),
        ('F', 'FULFILLED'),
        ('C', 'CANCELLED')
    )
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=1)
    order_date = models.DateTimeField(verbose_name='date ordered')
