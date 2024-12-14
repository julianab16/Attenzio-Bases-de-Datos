from django.contrib import admin
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^clase/', include('app.clase.urls')),
    re_path(r'^curso/', include('app.curso.urls')),
    re_path(r'^estudianteClase/', include('app.estudianteClase.urls')),
    re_path(r'^opcion/', include('app.opcion.urls')),
    re_path(r'^opcionEstudiante/', include('app.opcionEstudiante.urls')),
    re_path(r'^pregunta/', include('app.pregunta.urls')),
    re_path(r'^rol/', include('app.rol.urls')),
    re_path(r'^usuario/', include('app.usuario.urls'))
]

# Servir archivos de medios (solo en desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)