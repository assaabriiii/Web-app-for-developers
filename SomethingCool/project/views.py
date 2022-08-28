from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProjectForm
from .models import project

# Create your views here.
def mainPage(request) :
    return HttpResponse("The Main Page")

def projects(request) :
    projects = project.objects.all()
    context = {'project' : projects} 
    return render(request , 'project/project.html' , context)

def projectPK(request , pk) :
    projectObj = project.objects.get(id=pk)
    return render(request , "project/singleproject.html" , {"Key" : projectObj}) 

def create_project(request) :
    form = ProjectForm()
    context = {'form' : form}
    return render(request , "project/project_form.html" , context)