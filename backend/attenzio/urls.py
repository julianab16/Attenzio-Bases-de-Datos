from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^curso/', include('apps.curso.urls')),
    re_path(r'^estudianteClase/', include('apps.estudianteClase.urls')),
    re_path(r'^opcion/', include('apps.opcion.urls')),
    re_path(r'^opcionEstudiante/', include('apps.opcionEstudiante.urls')),
    re_path(r'^pregunta/', include('apps.pregunta.urls')),
    re_path(r'^rol/', include('apps.rol.urls')),
    re_path(r'^usuario/', include('apps.usuario.urls'))
]