from django.contrib import admin
from .models import Project, ProjectImage, ResumeItem, Category

admin.site.register(Project)
admin.site.register(ProjectImage)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    ordering = ("order",)
    search_fields = ("name",)

@admin.register(ResumeItem)
class ResumeItemAdmin(admin.ModelAdmin):
    list_display = ("category", "position", "title")
    list_editable = ("position",)
    list_filter = ("category",)
    ordering = ("category__order", "position", "id")
