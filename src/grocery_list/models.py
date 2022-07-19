from django.db import models

# Create your models here.
class List(models.Model):
    walmart_list = models.TextField(max_length=10000, null=True)
    broulims_list = models.TextField(max_length=10000, null=True)
    albertsons_list = models.TextField(max_length=10000, null=True)