from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = "pages/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context["latest_articles"] = Article.objects.all()[:5]
    #     return context
