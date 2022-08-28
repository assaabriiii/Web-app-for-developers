from django.shortcuts import render
from django.http import HttpResponse

from .models import project

# Create your views here.

projectList = [
    {
        "id" : "1" ,
        "Title" : "SQL",
        "Description" : "Stopped for a While"
    },
    {
        "id" : "2" ,
        "Title" : "CEH",
        "Description" : "Training Myself"
    },
    {
        "id" : "3" ,
        "Title" : "Backend Programming",
        "Description" : "Learning it"
    }
]

def mainPage(request) :
    return HttpResponse("The Main Page")

def projects(request) :
    projects = project.objects.all()
    context = {'project' : projects} 
    return render(request , 'project/project.html' , context)

def projectPK(request , pk) :
    projectObj = project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request , "project/singleproject.html" , {"Key" : projectObj , "tags" : tags}) 