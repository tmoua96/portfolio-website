from django.shortcuts import render, get_object_or_404
from .models import Project, Tag, Job, School
from django.db import OperationalError

# Create your views here.
def home(request):
    return render(request, "home.html")

def resume(request):
    try:
        jobs = Job.objects.all()
        schools = School.objects.all().order_by("-end_year")
    except OperationalError:
        experience = []
        education = []
    return render(request, "resume.html", {"jobs": jobs, "schools": schools})

def projects(request):
    try:
        projects = Project.objects.all()
        tags = Tag.objects.all().order_by("name")
    except OperationalError:
        projects = []
        tags = []
    return render(request, "projects.html", {"projects": projects, "tags": tags})

def project(request, id):
    try:
        project = get_object_or_404(Project, pk=id)
    except OperationalError:
        return render(request, "project.html", {"error": "Database error occurred."})
    return render(request, "project.html", {"project": project})

def contact(request):
    return render(request, "contact.html")