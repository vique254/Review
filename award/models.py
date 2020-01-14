from django.db import models

# Create your models here.
class Profile(models.Model):
   profile_photo=models.ImageField(upload_to='profile',height_field=200,width_field=200,default='')
   bio = models.CharField(max_length=200)
   
class   Image(models.Model):
    images =models.ImageField(upload_to='home')
    image_name = models.CharField(max_length=10)
    image_caption = models.CharField(max_length=250)
    profile = models.ForeignKey(Profile)
    likes = models.ManyToManyField('self', symmetrical = False)
    comments =models.TextField()