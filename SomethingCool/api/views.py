from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from project.models import project, review, Tag


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    Projects = project.objects.all()
    serializer = ProjectSerializer(Projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    Project = project.objects.get(id=pk)
    serializer = ProjectSerializer(Project, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    print("HELLO")
    PProject = project.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    Review, created = review.objects.get_or_create(
        owner=user,
        Project=PProject,
    )

    Review.value = data['value']
    Review.save()
    PProject.getVoteCount

    serializer = ProjectSerializer(PProject, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    projectId = request.data['project']

    Project = project.objects.get(id=projectId)
    tag = Tag.objects.get(id=tagId)

    Project.tags.remove(tag)

    return Response('Tag was deleted!')