from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import ProjectForm
from .models import project

# Create your views here.
def projects(request) :
    projects = project.objects.all()
    context = {'project' : projects} 
    return render(request , 'project/project.html' , context)

def projectPK(request , pk) :
    projectObj = project.objects.get(id=pk)
    return render(request , "project/singleproject.html" , {"Key" : projectObj}) 

def create_project(request) :
    form = ProjectForm()
    if request.method == 'POST' : 
        print(request.POST)
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid :
            form.save()
            return redirect('projects')
            
    context = {'form' : form }
    return render(request , "project/project_form.html" , context)

def update_project(request , pk) :
    projectObj = project.objects.get(id=pk)
    form = ProjectForm(instance=projectObj)
    if request.method == 'POST' : 
        print(request.POST)
        form = ProjectForm(request.POST , request.FILES, instance=projectObj )
        if form.is_valid :
            form.save()
            return redirect('projects')
            
    context = {'form' : form }
    return render(request , "project/project_form.html" , context)

def delete_project(request , pk) : 
    projectObj = project.objects.get(id=pk)
    if request.method == "POST" :
        projectObj.delete()
        return redirect('projects')
    context = {'object' : projectObj}
    return render(request , 'project/delete_confirm.html' , context)