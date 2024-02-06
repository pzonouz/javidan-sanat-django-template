from django.views.generic import TemplateView

from files.models import Image
from entities.models import Brand, Entity


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["TopSlideshow"] = Image.objects.filter(carousel=True)
        context["ProjectsSlideShow"] = Entity.objects.filter(type="PR")
        context["EventsSlideShow"] = Entity.objects.filter(type="EV")
        context["brands"] = Brand.objects.all()
        return context
