from django.db import models
import uuid
from users.models import Profile

# Create your models here.

class project(models.Model):
    owner = models.ForeignKey(Profile , null=True , blank=True , on_delete=models.SET_NULL) 
    
    id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True , editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True)
    demo_link = models.CharField(max_length=2000 , null=True , blank=True)
    src_link = models.CharField(max_length=2000 , null=True , blank=True)
    tags = models.ManyToManyField('Tag' , blank=True)
    vote_total = models.IntegerField(default=0 , null=True , blank=True)
    vote_ratio = models.IntegerField(default=0 , null=True , blank=True)
    
    fearured_img = models.ImageField(null=True , blank=True , default="default.jpg")

    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.title 
        
class review(models.Model) :
    vote_type = (
        ('up' , 'up vote'),
        ('down' , 'down vote')
    )
    #Owner
    Project = models.ForeignKey( project ,on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True , editable=False)
    body = models.TextField(blank=True , null=True)
    value = models.CharField(max_length=200 , choices=vote_type)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.value
    
    
class Tag(models.Model) :
    id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True , editable=False)
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name
     