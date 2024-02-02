from django.urls import path

from projects import views

app_name = "projects"

urlpatterns = [path("", views.AllProjects.as_view(), name="all")]
