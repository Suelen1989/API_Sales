from django.db import models
from uuid import uuid4

class Products(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    mark = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    registration_date = models.DateField()
    
