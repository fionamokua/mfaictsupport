from django.db import models
from users.models import CustomUser
# Create your models here.
class IctUser(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)