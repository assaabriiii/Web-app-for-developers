from django.forms import ModelForm
from .models import project

class ProjectForm(ModelForm) :
     class Meta :
        model = project
        fields = "__all__"