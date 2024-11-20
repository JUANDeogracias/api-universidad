# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.ViewSets.AlumnoViewSet import AlumnoViewSet
from api.ViewSets.RolViewSet import RolViewSet
from api.ViewSets.NotasViewSet import NotasViewSet
from api.ViewSets.ProfesorViewSet import ProfesorViewSet
from api.ViewSets.AsignaturasViewSet import AsignaturasViewSet

from rest_framework.documentation import include_docs_urls


# Crear el router para los ViewSets
router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet, basename='alumno')
router.register(r'roles', RolViewSet, basename='rol')
router.register(r'profesores', ProfesorViewSet, basename='profesor')
router.register(r'asignaturas', AsignaturasViewSet, basename='asignatura')
router.register(r'notas', NotasViewSet, basename='notas')

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='API Documentation')),
]