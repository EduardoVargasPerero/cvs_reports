from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PDFUploadView, CaracteristicaViewSet

"""
URLs de la aplicación para carga de archivos PDF y gestión del modelo Caracteristica.

Autor: Eduardo Vargas Perero  
Correo: eduardoevargasp@hotmail.com  
Fecha: 2025-06-12
"""

router = DefaultRouter()
router.register(r'caracteristicas', CaracteristicaViewSet)

urlpatterns = [
    path('subir-pdf/', PDFUploadView.as_view(), name='subir_pdf'),
     path('', include(router.urls)),
]