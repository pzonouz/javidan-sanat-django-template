from django.db import models
from core import models as core_models


class Image(core_models.TimeStamped):
    name = models.CharField(max_length=200)
    file = models.ImageField()
    carousel = models.BooleanField(default=False)
    link = models.CharField(max_length=150, null=True, blank=True)
    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="images",
    )
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="images",
    )
    event = models.ForeignKey(
        "events.Event",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="images",
    )
    projects = models.ManyToManyField(
        "projects.Project", blank=True, related_name="images"
    )

    def __str__(self):
        return self.name


class Video(core_models.TimeStamped):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=255, null=True)
    # file = models.FileField()
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="videos",
    )
    event = models.ForeignKey(
        "events.Event",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="videos",
    )
    projects = models.ManyToManyField(
        "projects.Project", related_name="videos", blank=True
    )

    def __str__(self):
        return self.name
