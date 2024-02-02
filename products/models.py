from core import models as core_models
from django.db import models


class Product(core_models.TimeStamped):
    name = models.CharField(max_length=100)
    preamble = models.TextField()
    level1 = models.ForeignKey(
        "ProductCategoryLevel1",
        on_delete=models.SET_NULL,
        null=True,
        related_name="products",
    )

    level2 = models.ForeignKey(
        "ProductCategoryLevel2",
        on_delete=models.SET_NULL,
        null=True,
        related_name="products",
    )
    level3 = models.ForeignKey(
        "ProductCategoryLevel3",
        on_delete=models.SET_NULL,
        null=True,
        related_name="products",
    )
    type = models.ForeignKey(
        "ProductType",
        on_delete=models.SET_NULL,
        null=True,
        related_name="products",
    )
    brand = models.ForeignKey(
        "Brand",
        on_delete=models.SET_NULL,
        null=True,
        related_name="products",
    )
    projects = models.ManyToManyField(to="projects.Project", related_name="products")

    def __str__(self) -> str:
        return self.name


class ProductCategoryLevel1(core_models.TimeStamped):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class ProductCategoryLevel2(core_models.TimeStamped):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class ProductCategoryLevel3(core_models.TimeStamped):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class ProductType(core_models.TimeStamped):
    name = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Brand(core_models.TimeStamped):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    small_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
