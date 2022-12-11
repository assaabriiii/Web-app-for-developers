from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer 
from project.models import project 



@api_view(['GET'])
def getRoutes(request) : 
    routes = [
        {"GET" : "api/project"},
        {"GET" : "api/project/id"},
        {"POST" : "api/project/id/vote"},
        {"POST" : "api/users/token"},
        {"POST" : "api/users/token/refresh"}
    ]
    return Response(routes)

@api_view(['GET'])
def getProjects(request) : 
    projects = project.objects.all()
    serializer = ProjectSerializer(projects , many=True) 
    
    return Response(serializer.data)