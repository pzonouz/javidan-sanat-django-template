from django.views.generic import ListView

from products.models import Product


class ProductsList(ListView):
    queryset = Product.objects.all()
