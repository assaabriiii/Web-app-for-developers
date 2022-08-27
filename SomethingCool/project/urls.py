from django.urls import path
from . import views

urlpatterns = [
    path('' , views.mainPage , name="mainPage"),
    path('projects' , views.projects , name="projects"),
    path('<str:pk>' , views.projectPK , name='projectPK')
]
