from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def projects(request) :
    return render(request , 'project/project.html')

def projectPK(request , pk) :
    return render(request , "project/singleproject.html")