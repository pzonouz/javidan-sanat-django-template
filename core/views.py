from django.views.generic import TemplateView

from files.models import Image
from products.models import Brand
from projects.models import Project
from events.models import Event


# Create your views here.
class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["TopSlideshow"] = Image.objects.filter(carousel=True)
        context["ProjectsSlideShow"] = Project.objects.all()
        context["EventsSlideShow"] = Event.objects.all()
        context["brands"] = Brand.objects.all()
        return context
