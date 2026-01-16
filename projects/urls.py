from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_projects/', views.all_projects, name='all_projects'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('resume/', views.resume, name='resume'),
    path('certificates/', views.certificates, name='certificates'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)