from django.forms import ModelForm
from .models import project

class ProjectForm(ModelForm) :
     class Meta :
        model = project
        fields = ['title' , 'description' , 'demo_link' , 'src_link' , 'tags' , 'fearured_img' ]