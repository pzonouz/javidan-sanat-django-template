from django.db import models
from core import models as core_models


class Customer(core_models.TimeStamped):
    name = models.CharField(max_length=50)
    description = models.TextField()
    city = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    products = models.ManyToManyField(
        to="products.Product", related_name="customers", blank=True
    )

    def __str__(self):
        return self.name
