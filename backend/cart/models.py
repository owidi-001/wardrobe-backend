from django.db import models

from customer.models import Customer

from core.models import Product


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(verbose_name='creation date')
    checked_out = models.BooleanField(default=False, verbose_name='checked out')

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'
        ordering = ('-creation_date',)


class Item(models.Model):
    cart = models.ForeignKey(Cart, verbose_name='cart', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ('cart',)

    def total_price(self):
        return self.quantity * self.product.price

    total_price = property(total_price)
