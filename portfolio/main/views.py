from django.shortcuts import render, get_object_or_404
from .models import Project, Tag
from django.db import OperationalError

# Create your views here.
def home(request):
    try:
        projects = Project.objects.all()
        tags = Tag.objects.all().order_by("name")
    except OperationalError:
        projects = []
        tags = []
    return render(request, "home.html", {"projects": projects, "tags": tags})

def about(request):
    return render(request, "about.html")

def project(request, id):
    try:
        project = get_object_or_404(Project, pk=id)
    except OperationalError:
        return render(request, "project.html", {"error": "Database error occurred."})
    return render(request, "project.html", {"project": project})