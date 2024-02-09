from django.views.generic import TemplateView
from django.db.models import F


from files.models import Image
from entities.models import Brand, Entity


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topSlideshow_entities = (
            Entity.objects.annotate(link=F("pk"))
            .annotate(file=F("main_picture"))
            .filter(carousel=True)
        )
        topSlideshow_images = Image.objects.filter(carousel=True)
        topSlideshow = list(topSlideshow_entities) + list(topSlideshow_images)
        context["TopSlideshow"] = topSlideshow
        context["ProjectsSlideShow"] = Entity.objects.filter(type="PR")
        context["EventsSlideShow"] = Entity.objects.filter(type="EV")
        context["brands"] = Brand.objects.all()
        return context
