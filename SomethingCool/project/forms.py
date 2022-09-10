from django.forms import ModelForm , widgets
from .models import project 
from django import forms
class ProjectForm(ModelForm) :
   class Meta :
      model = project
      fields = ['title',  'description' , 'demo_link' , 'src_link' , 'tags' , 'fearured_img' ]
      widgets = {
         'tags' : forms.CheckboxSelectMultiple(),
      }
   
   def __init__(self , *args , **kwargs) :
         super(ProjectForm , self).__init__(*args , **kwargs)
         
         # self.fields['title'].widget.attrs.update({'class' : 'input' , 'placeholder' : 'Add Title'})
         # self.fields['description'].widget.attrs.update({'class' : 'input' , 'placeholder' : 'Add Description'})
         
         for name , field in self.fields.items() :
            field.widget.attrs.update({'class' : 'input'})
      