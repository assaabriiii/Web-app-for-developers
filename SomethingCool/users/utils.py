from .models import Profile , Skill
from django.db.models import Q

def search_profile(request) :
    search_result = ''
    
    if request.GET.get('search_result') :
        search_result = request.GET.get('search_result')
        
    skill = Skill.objects.filter(name__icontains=search_result)    
    
    Profiles = Profile.objects.distinct().filter(Q(name__icontains=search_result) |
                                                 Q(username__icontains=search_result) |
                                                 Q(skill__in=skill))
    
    return Profiles , search_result 