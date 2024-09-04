from django.contrib import admin
from .models import Tag, Project, ProjectImage, Contact, Job, School
from django.utils.html import mark_safe

# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    readonly_fields = ("display_image",)

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="192" height="108" />')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    inlines = [ProjectImageInline]
    search_fields = ("title", "description")
    list_filter = ("tags",)

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Job)
admin.site.register(School)
