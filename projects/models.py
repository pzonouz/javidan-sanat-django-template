from django.db import models
from core import models as core_models


class Project(core_models.TimeStamped):
    name = models.CharField(max_length=200)
    description = models.TextField()
    main_picture = models.ImageField(null=True, blank=True)
    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.SET_NULL,
        null=True,
        related_name="projects",
    )

    def __str__(self):
        return self.name
