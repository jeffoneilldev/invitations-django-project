from django.db import models
from products.models import Product

# Create your models here.
class Order(models.Model):
    partner1_full_name = models.CharField(max_length=50, blank=False)
    partner2_full_name = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    phone_number = models.CharField(max_length=20, blank=False)
    contact_email = models.CharField(max_length=20, blank=False)
    street_address1 = models.CharField(max_length=80, blank=False)
    street_address2 = models.CharField(max_length=80, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    wedding_date = models.DateField()
    ceremony_address = models.CharField(max_length=80, blank=False)
    reception_address = models.CharField(max_length=80, blank=False)
    rsvp_date = models.DateField()
    

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.partner1_full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)
