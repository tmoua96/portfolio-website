from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path("skills/", views.skills, name="skills"),
    path("about/", views.about, name="about"),
    path("projects/<int:id>", views.project, name="project"),
]
