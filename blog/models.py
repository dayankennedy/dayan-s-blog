from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    user=models.ForeignKey(User,blank=False,on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    body=models.TextField(max_length=255, blank=True, null=True)
    date_posted= models.DateField(auto_now_add=True)
    image=models.ImageField(null=True, upload_to='images/',default='images/default.jpg')
    
    def __str__(self):
        return self.body ,self.title
