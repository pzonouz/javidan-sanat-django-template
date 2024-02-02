from django.db import models
from core import models as core_models


class Project(core_models.TimeStamped):
    name = models.CharField(max_length=100)
    description = models.TextField()
    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.SET_NULL,
        null=True,
        related_name="projects",
    )
