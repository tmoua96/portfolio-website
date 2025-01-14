from django.shortcuts import render, get_object_or_404
from .models import Project, Tag, Job, School, Contact
from django.db import OperationalError
from django.http import JsonResponse
from django.core.mail import EmailMessage
from smtplib import SMTPException
from django.conf import settings
from .forms import ContactForm
from .utils import is_english

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
        projects = Project.objects.all().order_by("-priority", "title")
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
            form = ContactForm(request.POST)

            if form.is_valid():
                # process the data in form.cleaned_data as required
                # make contact object without saving to database just yet
                contact: Contact = form.save(commit=False)

                if is_english(contact.message):
                    full_message = f"{contact.name} ({contact.email}) says:\n\n{contact.message}"

                    email = EmailMessage(
                        subject=contact.subject,
                        body=full_message,
                        from_email=settings.EMAIL_HOST_USER,
                        to=[settings.EMAIL_HOST_USER],
                        reply_to=[contact.email]
                    )

                    email.send(fail_silently=False)

                contact.save()
                
                return JsonResponse({"success": True, "message": "Message sent successfully."}, status=200)
            else:
                message: str = "Error sending message. Ensure all fields are filled correctly."
                return JsonResponse({"success": False, "message": message, "errors": form.errors}, status=400)
        except SMTPException as e:
            message: str = "Unable to send. An error occurred while sending the email. Please try again later."
            return JsonResponse({"success": False, "message": message, "exception": e}, status=400)
        except Exception as e:
            message: str = "Error sending message."
            return JsonResponse({"success": False, "message": message, "exception": e}, status=400)
    
    return render(request, "contact.html")
