from django.db.models import Q 
from .models import project , Tag

def project_search(request) :
    search_result = ""
    
    if request.GET.get('search_result') :
        search_result = request.GET.get('search_result') 
    
    tags = Tag.objects.filter(name__icontains=search_result)
    
    projects = project.objects.distinct().filter(Q(title__icontains=search_result) |
                                                 Q(description__icontains=search_result) |
                                                 Q(tags__in=tags) |
                                                 Q(owner__name__icontains=search_result)) 
    
    return projects , search_result