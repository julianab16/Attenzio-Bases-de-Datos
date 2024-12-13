from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path
from . import views
from .views import *

urlpatterns = [
    re_path('', views.home, name='home')
]

