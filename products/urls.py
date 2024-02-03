from django.urls import path
from products.views import ProductsList

app_name = "products"

urlpatterns = [path("", ProductsList.as_view(), name="list")]
