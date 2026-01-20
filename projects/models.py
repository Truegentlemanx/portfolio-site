from django.db import models

# Create your models here.
class Project(models.Model):
    """Class that represents a Project model."""
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"

class ProjectImage(models.Model):
    """Class representing images related to a project."""
    project = models.ForeignKey(Project, related_name="images", 
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/details/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.project.title} image"
    
class ResumeItem(models.Model):
    """Class representing resume items like education and employers"""
    category = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Title: {self.title} Category: {self.category}"
