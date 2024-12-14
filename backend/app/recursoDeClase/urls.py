from django.urls import path
from . import views

urlpatterns = [
    path('create-recurso/<int:clase_id>/', views.create_recurso, name='create-recurso'),
    path('success/', views.success, name='success'),  # Agrega una vista de éxito
]