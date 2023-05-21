from django.urls import path
from .views import *
urlpatterns=[
     path('liststudent', liststudent),
     path('liststaff', liststaff),
     path('link', link),

]