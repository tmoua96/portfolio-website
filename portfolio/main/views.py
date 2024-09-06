from django.shortcuts import render, get_object_or_404
from .models import Project, Tag, Job, School, Contact
from django.db import OperationalError
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, "home.html")

def resume(request):
    try:
        jobs = Job.objects.all()
        schools_query = School.objects.all().order_by("-end_year")
        schools = [schools_query[0]] if len(schools_query) > 0 else []
    except OperationalError:
        jobs = []
        schools = []
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
    if request.method == "POST":
        try:
            name = request.POST["name"]
            email = request.POST["email"]
            subject = request.POST["subject"]
            message = request.POST["message"]
        except KeyError:
            return render(request, "contact.html")
        
        # TODO: still need to add actual validation
        if not settings.IS_DEVELOPMENT:
            Contact.objects.create(name=name, email=email, subject=subject, message=message)

        send_mail(
            subject,
            f'From {name}:\n{message}',
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return JsonResponse({"message": "Thank you for your message!"})
    
    return render(request, "contact.html")