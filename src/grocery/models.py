from time import timezone
from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=120)
    quantity = models.CharField(max_length=50, null=True)
    walmart_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    broulims_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    albertsons_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    last_updated = models.DateField( auto_now=False, auto_now_add=False, default=timezone.now())