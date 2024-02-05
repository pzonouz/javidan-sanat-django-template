from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.db.models import Q

from products.models import Category, Product


class ProductsList(View):
    def get(self, request, *args, **kwargs):
        part_categories = Category.objects.filter(product__type="PT").distinct()
        service_categories = Category.objects.filter(product__type="SR").distinct()
        class_categories = Category.objects.filter(product__type="CL").distinct()
        if not request.GET:
            parts = Product.objects.all()
            return render(
                request,
                "products/product_list.html",
                context={
                    "parts": parts,
                    "product_type": "PT",
                    "part_categories": part_categories,
                    "service_categories": service_categories,
                    "class_categories": class_categories,
                },
            )
        # search = request.GET.get("search")
        # if search is not None:
        #     products = Product.objects.filter(name__icontains=search)
        #     return render(
        #         request,
        #         "products/product_list.html",
        #         context={"products": products},
        #     )

        product_type = request.GET.get("product_type")
        category = request.GET.get("category")
        vehicle = request.GET.get("vehicle")
        my_q = Q()
        if product_type != "":
            my_q = Q(type=product_type)
        if category != "":
            my_q &= Q(category=category)
        if vehicle != "":
            my_q &= Q(vehicle=vehicle)
        parts = Product.objects.filter(my_q)
        return render(
            request,
            "products/product_list.html",
            context={
                "parts": parts,
                "part_categories": part_categories,
                "service_categories": service_categories,
                "class_categories": class_categories,
                "product_type": product_type,
                "part_category": category,
                "vehicle": vehicle,
            },
        )


class ProductDetail(DetailView):
    model = Product
