from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path

from .views import *

urlpatterns = [
  re_path(r'$', ListCreateOpcion.as_view(), name='create-list-opcion')
]

urlpatterns = format_suffix_patterns(urlpatterns)