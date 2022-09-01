from multiprocessing import context
from urllib import request
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Profile
# Create your views here.

def profiles(request) :
    Profiles = Profile.objects.all()
    context = {'profiles' : Profiles}
    return render(request , 'users/profiles.html' , context)


def user_profile(request , pk) :
    user = Profile.objects.get(id=pk)
    context ={'user' : user}
    return render(request , 'users/user-profile.html' , context)