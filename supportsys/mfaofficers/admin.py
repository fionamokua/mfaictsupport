from django.contrib import admin
from .models import MfaofficerUser
# Register your models here.
class MfaofficerAdmin(admin.ModelAdmin):
   list_display=['get_username','get_email',]
   def get_username(self,obj):
      return obj.user.username
   get_username.short_description='MFA-Officer Username'
   def get_email(self,obj):
      return obj.user.email
   get_email.short_description='MFA-Officer email'
admin.site.register(MfaofficerUser,MfaofficerAdmin)