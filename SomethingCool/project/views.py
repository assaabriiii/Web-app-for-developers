from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def projects(request , pk) :
    return HttpResponse("Project" + " " +pk)