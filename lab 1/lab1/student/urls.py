from django.urls import path
from .views import *
urlpatterns=[
    path('', index),
    path('insert/',insert),
    path('update/',update),
    path('delete/',delete),


]