from django.urls import path
from .views import ClientTaskForm
urlpatterns=[
    path('taskform',ClientTaskForm.as_view(),name='taskform')
]