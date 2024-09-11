from typing import Any
from typing import Iterable
from django.db import models
import os
from django.core.exceptions import ValidationError

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)
    thumbnail = models.ImageField(upload_to="project_thumbnails/", blank=True)

    def __str__(self) -> str:
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Job(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    start_year = models.IntegerField(null=False)
    end_year = models.IntegerField(null=True)
    description = models.TextField()
    city = models.CharField(max_length=30, null=False)
    state = models.CharField(max_length=30, null=False)

    def __str__(self) -> str:
        return self.title
    
class School(models.Model):
    name = models.CharField(max_length=50, null=False)
    degree = models.CharField(max_length=30)
    major = models.CharField(max_length=30, null=True)
    start_year = models.IntegerField(null=False)
    end_year = models.IntegerField(null=True)
    description = models.TextField()
    city = models.CharField(max_length=30, null=False)
    state = models.CharField(max_length=30, null=False)

    def __str__(self) -> str:
        return self.name