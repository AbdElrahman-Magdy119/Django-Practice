from django.urls import path
from .views import *
urlpatterns=[
    path('', index),
    path('delete/',delete),
    path('update/',update),
    path('insert/',insert)

]