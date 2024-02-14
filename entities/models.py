from django.urls import reverse
from core import models as core_models
from django.db import models

TYPE_CHOICES = (
    ("PT", "PART"),
    ("SR", "SERVICE"),
    ("CL", "CLASS"),
    ("PR", "PROJECT"),
    ("EV", "EVENT"),
)
VEHICLE_CHOICES = (("HV", "HEAVY"), ("LT", "LIGHT"))


class Entity(core_models.TimeStamped):
    name = models.CharField(max_length=100)
    preamble = models.TextField()
    main_picture = models.ImageField(null=True)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, null=True)
    carousel = models.BooleanField(default=False)

    brand = models.ForeignKey(
        "Brand",
        on_delete=models.SET_NULL,
        null=True,
        related_name="entities",
        blank=True,
    )
    categories = models.ManyToManyField(to="category", related_name="entities")
    entities = models.ManyToManyField(to="self", blank=True)
    vehicle = models.CharField(max_length=10, choices=VEHICLE_CHOICES, default="LT")

    def get_absolute_url(self):
        return reverse("entities:detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name


class Brand(core_models.TimeStamped):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    small_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Specification(core_models.TimeStamped):
    field = models.TextField()
    entities = models.ManyToManyField(to=Entity, related_name="specifications")

    def __str__(self) -> str:
        return self.field
