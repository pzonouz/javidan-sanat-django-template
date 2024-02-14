from django.urls import path
from entities.views import BrandRelatedEntities, EntitiesList, EntityDetail

app_name = "entities"

urlpatterns = [
    path("", EntitiesList.as_view(), name="list"),
    path("<int:pk>", EntityDetail.as_view(), name="detail"),
    path("brands/<int:pk>", BrandRelatedEntities.as_view(), name="brands-detail"),
]
