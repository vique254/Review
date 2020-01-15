from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from tinymce.models import HTMLField
# Create your models here.
class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   profile_photo=models.ImageField(upload_to='images',default='person.png',blank=True)
   bio = models.CharField(max_length=200)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
        
class   Project(models.Model):
    images =models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=10)
    image_caption = models.CharField(max_length=250)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    likes = models.ManyToManyField('self', symmetrical = False)
    comments =HTMLField()
    
    @classmethod
    def search_by_profile(cls,search_term):
        award = cls.objects.filter(title__icontains=search_term)
        return award