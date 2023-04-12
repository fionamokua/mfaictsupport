from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db.models.signals import m2m_changed, post_save,post_delete
from django.db import transaction
from django.dispatch import receiver
from django.contrib.auth.models import  Group
from ictsupport.models import IctUser
from mfaofficers.models import MfaofficerUser
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=('email','username')
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=get_user_model()
        fields=('email','username')
    @transaction.atomic  
    @receiver(m2m_changed)
    def groupfieldadded(action,pk_set,model,instance,**kwargs):
                if model == Group:
                    
                    if action == 'post_remove':
                            if instance.groups.filter(name='ictsupport').exists():

                                pass
                            else:
                                try:
                                    instance.save()
                                    u= IctUser.objects.get(user=instance)
                                    u.delete()
                                except:
                                    instance
                            if instance.groups.filter(name='mfa-officer').exists():

                                pass
                            else:
                                try:
                                    instance.save()
                                    u= MfaofficerUser.objects.get(user=instance)
                                    u.delete()
                                except:
                                    instance
                           
                    
                                
                    if action == 'post_add':
                            if instance.groups.filter(name='mfa-officer').exists():
                                if MfaofficerUser.objects.filter(user=instance).exists():
                                    pass
                                else:

                                    mfaofficergroup= Group.objects.get(name='mfa-officer')

                                    mfaofficergroup.user_set.add(instance)
                                    instance.save()
                                    MfaofficerUser.objects.create(user=instance)
                           
                            if instance.groups.filter(name='ictsupport').exists():
                                if IctUser.objects.filter(user=instance).exists():
                                    pass
                                else:

                                    ictsupportgroup= Group.objects.get(name='ictsupport')

                                    ictsupportgroup.user_set.add(instance)
                                    instance.save()
                                    IctUser.objects.create(user=instance)
                          