from django.db import models

# Create your models here.
class List(models.Model):
    store = models.CharField(max_length=50)
    quantity = models.IntegerField()
    item_id = models.IntegerField(null=False)