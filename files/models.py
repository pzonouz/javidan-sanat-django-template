from django.db import models
from core import models as core_models


class Image(core_models.TimeStamped):
    name = models.CharField(max_length=50)
    file = models.ImageField()
    carousel = models.BooleanField(default=False)
    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.SET_NULL,
        null=True,
        related_name="images",
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.SET_NULL, null=True, related_name="images"
    )
    event = models.ForeignKey(
        "events.Event", on_delete=models.SET_NULL, null=True, related_name="images"
    )
    projects = models.ManyToManyField("projects.Project", related_name="images")


class Video(core_models.TimeStamped):
    name = models.CharField(max_length=50)
    file = models.FileField()
    product = models.ForeignKey(
        "products.Product", on_delete=models.SET_NULL, null=True, related_name="videos"
    )
    event = models.ForeignKey(
        "events.Event", on_delete=models.SET_NULL, null=True, related_name="videos"
    )
    projects = models.ManyToManyField("projects.Project", related_name="videos")
