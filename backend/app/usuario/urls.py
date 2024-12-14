
from django.urls import re_path
from . import views
from .views import *

urlpatterns = [
      re_path('', views.loginStudent, name='loginStudent')
]

