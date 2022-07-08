from django.shortcuts import render
from.models import Project, MyInfo

def home(request):
    projects = Project.objects.all()
    my_info = MyInfo.objects.get()
    return render(request, 'portfolio/home.html', {'projects': projects, 'info': my_info})
