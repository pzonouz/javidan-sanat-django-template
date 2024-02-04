from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from products.models import Product


class ProductsList(View):
    def get(self, request, *args, **kwargs):
        if not request.GET:
            products = Product.objects.all()
            return render(
                request, "products/product_list.html", context={"products": products}
            )


class ProductDetail(DetailView):
    model = Product
