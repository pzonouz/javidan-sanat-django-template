from core import models as core_models
from django.db import models

TYPE_CHOICES = (("PR", "PRODUCT"), ("SR", "SERVICE"), ("CL", "CLASS"))


class Product(core_models.TimeStamped):
    name = models.CharField(max_length=100)
    preamble = models.TextField()
    main_picture = models.ImageField(null=True)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, null=True)

    brand = models.ForeignKey(
        "Brand",
        on_delete=models.SET_NULL,
        null=True,
        related_name="products",
    )
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    projects = models.ManyToManyField(
        to="projects.Project", related_name="products", blank=True
    )

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
