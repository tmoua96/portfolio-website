from django.contrib import admin
from .models import Tag, Project, Contact, Job, School
from django.utils.html import mark_safe

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    search_fields = ("title", "description")
    list_filter = ("tags",)
    readonly_fields = ("display_image",)
    
    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.thumbnail.url}" width="100" height="100" />')

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Job)
admin.site.register(School)
