from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

projectList = [
    {
        "id" : 1 ,
        "Title" : "SQL",
        "Description" : "Stopped for a While"
    },
    {
        "id" : 2 ,
        "Title" : "CEH",
        "Description" : "Training Myself"
    },
    {
        "id" : 3 ,
        "Title" : "Backend Programming",
        "Description" : "Learning it"
    }
]

def mainPage(request) :
    return HttpResponse("The Main Page")

def projects(request) :
    page = "projects"
    number = 11
    context = {'page' : page , 'number' : number , 'projectList' : projectList} 
    return render(request , 'project/project.html' , context)

def projectPK(request , pk) :
    return render(request , "project/singleproject.html")