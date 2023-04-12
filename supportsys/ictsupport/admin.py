from django.contrib import admin
from .models import IctUser
# Register your models here.
class Ictusersadmin(admin.ModelAdmin):
   list_display=['get_username','get_email',]
   def get_username(self,obj):
      return obj.user.username
   get_username.short_description='ICTSupport Username'
   def get_email(self,obj):
      return obj.user.email
   get_email.short_description='ICTSuport email'

admin.site.register(IctUser,Ictusersadmin)