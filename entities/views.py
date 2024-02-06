from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.db.models import Q

from entities.models import Category, Entity


class EntitiesList(View):
    def get(self, request, *args, **kwargs):
        part_categories = Category.objects.filter(entity__type="PT").distinct()
        service_categories = Category.objects.filter(entity__type="SR").distinct()
        class_categories = Category.objects.filter(entity__type="CL").distinct()
        project_categories = Category.objects.filter(entity__type="PR").distinct()
        event_categories = Category.objects.filter(entity__type="EV").distinct()
        if not request.GET:
            entities = Entity.objects.filter(type="PT")
            return render(
                request,
                "entities/entity_list.html",
                context={
                    "entities": entities,
                    "entity_type": "PT",
                    "part_categories": part_categories,
                    "service_categories": service_categories,
                    "class_categories": class_categories,
                    "project_categories": project_categories,
                    "event_categories": event_categories,
                },
            )
        # search = request.GET.get("search")
        # if search is not None:
        #     entities = Entity.objects.filter(name__icontains=search)
        #     return render(
        #         request,
        #         "entities/entity_list.html",
        #         context={"entities": entities},
        #     )

        entity_type = request.GET.get("entity_type")
        category = request.GET.get("category")
        vehicle = request.GET.get("vehicle")
        my_q = Q()
        if entity_type != "":
            my_q = Q(type=entity_type)
        if category != "":
            my_q &= Q(category=category)
        if vehicle != "":
            my_q &= Q(vehicle=vehicle)
        entities = Entity.objects.filter(my_q)
        return render(
            request,
            "entities/entity_list.html",
            context={
                "entities": entities,
                "part_categories": part_categories,
                "service_categories": service_categories,
                "class_categories": class_categories,
                "project_categories": project_categories,
                "event_categories": event_categories,
                "entity_type": entity_type,
                "entity_category": category,
                "vehicle": vehicle,
                "category": category,
            },
        )


class EntityDetail(DetailView):
    model = Entity
