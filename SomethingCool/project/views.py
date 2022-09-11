from django.shortcuts import render , redirect
from .forms import ProjectForm
from .models import project 
from django.contrib.auth.decorators import login_required
from .utils import project_search


# Create your views here.
def projects(request) :
    search_result = ""
    projects , search_result = project_search(request)
    context = {'project' : projects , 'search_result' : search_result}  
    return render(request , 'project/project.html' , context)

def projectPK(request , pk) :
    projectObj = project.objects.get(id=pk)
    return render(request , "project/singleproject.html" , {"Key" : projectObj}) 

@login_required(login_url="login")
def create_project(request) :
    
    profile = request.user.profile
    
    form = ProjectForm()
    
    if request.method == 'POST' : 
        print(request.POST)
        form = ProjectForm(request.POST , request.FILES)
        
        if form.is_valid :
            project = form.save(commit=False)
            project.owner = profile
            
            project.save()
            return redirect('projects')
            
    context = {'form' : form }
    return render(request , "project/project_form.html" , context)

@login_required(login_url="login")
def update_project(request , pk) :
    
    profile = request.user.profile
    
    # projectObj = project.objects.get(id=pk)
    
    projectObj = profile.project_set.get(id=pk)
    form = ProjectForm(instance=projectObj)
    if request.method == 'POST' : 
        print(request.POST)
        form = ProjectForm(request.POST , request.FILES, instance=projectObj )
        if form.is_valid :
            form.save()
            return redirect('projects')
            
    context = {'form' : form }
    return render(request , "project/project_form.html" , context)

@login_required(login_url="login")
def delete_project(request , pk) : 
    
    profile = request.user.profile
    
    # projectObj = project.objects.get(id=pk)
    
    projectObj = profile.project_set.get(id=pk)
    if request.method == "POST" :
        projectObj.delete()
        return redirect('projects')
    context = {'object' : projectObj}
    return render(request , 'project/delete_confirm.html' , context)