from django.shortcuts import render
from .models import Project, ProjectImage, ResumeItem
from django.db.models import F

# Create your views here.
def all_projects(request):
    # query the db to return all project objects.
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/all_projects.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    project_img = ProjectImage.objects.filter(project=project)
    context = {'project': project, 'project_img': project_img}
    return render(request, 'projects/detail.html', context)

def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/index.html', context)

def resume(request):
    resume_items = ResumeItem.objects.exclude(
        title=F("category"), category="Certificate").order_by("category", "-start_date", 
                                               "-end_date", "title")
    context = {'resume_items': resume_items}
    return render(request, 'projects/resume.html', context)

def certificates(request):
    resume_item = ResumeItem.objects.filter(category="Certificate").order_by("-end_date", "title")
    context = {'resume_items': resume_item}
    return render(request, 'projects/certificates.html', context)

def about_me(request):
    resume_item = ResumeItem.objects.all()
    context = {'resume_item': resume_item}
    return render(request, 'projects/about_me.html', context)