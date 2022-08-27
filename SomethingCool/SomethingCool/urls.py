from django.urls import path,include
from django.contrib import admin
from django.http import HttpResponse

    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/' , include('project.urls'))
]
