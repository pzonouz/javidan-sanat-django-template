from django.urls import path
from products.views import ProductsList, ProductDetail

app_name = "products"

urlpatterns = [
    path("", ProductsList.as_view(), name="list"),
    path("<int:pk>", ProductDetail.as_view(), name="detail"),
]
