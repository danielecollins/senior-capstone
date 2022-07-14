from time import timezone
from unicodedata import decimal, name
from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=120)
    quantity = models.CharField(max_length=50, null=True)
    walmart_price = models.DecimalField(max_digits=5, decimal_places=2)
    broulims_price = models.DecimalField(max_digits=5, decimal_places=2)
    albertsons_price = models.DecimalField(max_digits=5, decimal_places=2)
    last_updated = models.DateField( auto_now=False, auto_now_add=False, default=timezone.now())