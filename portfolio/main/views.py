from django.shortcuts import render, get_object_or_404
from .models import Project, Tag, Job, School, Contact
from django.db import OperationalError
from django.http import JsonResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
import logging

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
        projects = Project.objects.all().order_by("id")
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
            # TODO: still need to add actual validation
            name = request.POST["name"]
            from_email = request.POST["email"]
            subject = request.POST["subject"]
            message = request.POST["message"]

            if name and from_email and subject and message:
                full_message = f"{name} ({from_email}) says:\n\n{message}"

                Contact.objects.create(name=name, email=from_email, subject=subject, message=message)

                email = EmailMessage(
                    subject=subject,
                    body=full_message,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER],
                    reply_to=[from_email]
                )

                email.send(fail_silently=False)
            else:
                return render(request, "contact.html", {"error": "An error occurred. Please try again later."}, status=400)
        except KeyError:
            return render(request, "contact.html", status=400)
        except:
            logger = logging.getLogger(__name__)
            logger.error("An error occurred while sending the email.", exc_info=True)
            return render(request, "contact.html", {"error": "An error occurred. Please try again later."}, status=400)
    
    return render(request, "contact.html")