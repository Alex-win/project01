from django.urls import path
from ex1.views import *

urlpatterns =[
    path('homepage/',my_homepage,name='homepage'),
    path('homepage/register/',my_register,name='register')

]