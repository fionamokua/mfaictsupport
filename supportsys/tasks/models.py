from django.db import models
from mfaofficers.models import MfaofficerUser
# Create your models here.
class Task(models.Model):
    officenumber=models.IntegerField()
    email=models.ForeignKey(MfaofficerUser,on_delete=models.CASCADE)
    TASK_CHOICES = (
    ("internet", "internet"),
    ("computer_issue", "computer_issue"),
    ("request meeting", "request meeting"),
    ("other", "other"),
   
)
    natureofproblem=  models.CharField(
        max_length = 20,
        choices = TASK_CHOICES,
        default = 'internet'
        )
    directorate=models.TextField(max_length=50)
    division=models.TextField(max_length=50)
    station=models.TextField(max_length=50)
    taskdescription=models.TextField(max_length=200, default='Describe here nature of problem')