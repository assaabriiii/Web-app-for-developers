from django.shortcuts import render , redirect
from .models import Profile
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomUserCreationForm

# Create your views here.

def login_user(request) :
    page = 'login'
    
    # Don't let the login user see the login page and 
    # redirect them to profiles page 
    if request.user.is_authenticated :
        return redirect('profiles')
    
    if request.method == 'POST' : 
        username = request.POST['username']
        password = request.POST['password']
        
        try :
            user = User.objects.get(username=username)
        except :
            print("L")
        
        user = authenticate(request , username=username , password=password)
        
        # redirect logined user to profiles page 
        if user is not None :
            login(request , user)
            return redirect('profiles')
        else :
            messages.error(request , message="Whopsie You Did Something Wrong 😳")
        
        
    return render(request , 'users/login-register.html')

def logout_user(request) :
    logout(request)
    messages.error(request , message="Logged out fortunatly 🥹")
    return redirect('login')


def register_user(request) :
    page = 'register'
    form = CustomUserCreationForm()
    
    
    if request.method == "POST" :
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid() :
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request , 'User Account has Been created')
            login(request , user)
            return redirect('profiles')
        else :
            messages.error(request , "Error :<")
        
    
    context = {'page' : page , 'form' : form}
    return render(request , 'users/login-register.html' , context)



def profiles(request) :
    Profiles = Profile.objects.all()
    context = {'profiles' : Profiles}
    return render(request , 'users/profiles.html' , context)


def user_profile(request , pk) :
    user = Profile.objects.get(id=pk)
    context ={'user' : user}
    return render(request , 'users/user-profile.html' , context)