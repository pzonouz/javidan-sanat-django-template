from django.db import models
from core import models as core_models


class Event(core_models.TimeStamped):
    name = models.CharField(max_length=50)
    description = models.TextField()
    main_picture = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
