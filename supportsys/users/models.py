from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import  Group

# Create your models here.
class  CustomUser(AbstractUser):
    pass
@receiver(post_save, sender=CustomUser,)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='mfa-officer'))