from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    project_image = models.ImageField(upload_to = 'projects/')
    caption = models.CharField(max_length=250)
    project_link = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()
        
    @classmethod
    def search_by_title(cls,search_term):
        award = cls.objects.filter(title__icontains=search_term)
        return award    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_photo = models.ImageField(upload_to = 'profiles/')
    bio = models.TextField(max_length=255)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def updateProfile(sender, **kwargs):
        if kwargs['created']:
            profile = Profile.objects.created(user=kwargs['instance'])

            post_save.connect(Profile, sender=User)