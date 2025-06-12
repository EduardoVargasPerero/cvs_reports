from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PDFUploadSerializer

from rest_framework import viewsets
from .models import Caracteristica
from .serializers import CaracteristicaSerializer

import fitz
import unicodedata
import re

"""
Vistas para la API REST:
- Procesamiento de archivos PDF para extraer texto, validar características y obtener datos de contacto.
- Gestión CRUD del modelo Caracteristica.

Autor: Eduardo Vargas Perero  
Correo: eduardoevargasp@hotmail.com  
Fecha: 2025-06-12
"""

def normalizar_texto(texto):
    texto = texto.upper()
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    return texto



def extraer_info_contacto(texto):
    info = {}

    # Correos electrónicos
    correos = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)
    info["correos"] = correos

    # Teléfonos (formato flexible: 10+ dígitos, con guiones o espacios)
    telefonos = re.findall(r'\b(?:\+?\d{1,3})?[ -.]?\(?\d{2,4}\)?[ -.]?\d{3,4}[ -.]?\d{3,4}\b', texto)
    info["telefonos"] = telefonos

    # GitHub
    githubs = re.findall(r'https?://(www\.)?github\.com/[A-Za-z0-9_.-]+', texto)
    info["github"] = githubs

    # LinkedIn
    linkedins = re.findall(r'https?://(www\.)?linkedin\.com/in/[A-Za-z0-9_.-]+', texto)
    info["linkedin"] = linkedins

    return info


class PDFUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PDFUploadSerializer(data=request.data)
        if serializer.is_valid():
            archivos = serializer.validated_data['archivos']
            caracteristicas = list(Caracteristica.objects.values_list('texto', flat=True))
            caracteristicas_normalizadas = [normalizar_texto(c) for c in caracteristicas]

            aprobados = []
            rechazados = []

            for archivo in archivos:
                if archivo.content_type != 'application/pdf':
                    rechazados.append({'archivo': archivo.name, 'error': 'No es un PDF'})
                    continue

                texto = self.extraer_texto_pdf(archivo)
                texto_normalizado = normalizar_texto(texto)

                if any(c in texto_normalizado for c in caracteristicas_normalizadas):
                    info_contacto = extraer_info_contacto(texto)
                    aprobados.append({
                        'archivo': archivo.name,
                        'contacto': info_contacto
                    })
                else:
                    rechazados.append({'archivo': archivo.name, 'error': 'No contiene características'})

            return Response({
                'aprobados': aprobados,
                'rechazados': rechazados
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def extraer_texto_pdf(self, archivo):
        contenido = ""
        with fitz.open(stream=archivo.read(), filetype="pdf") as doc:
            for pagina in doc:
                contenido += pagina.get_text()
        return contenido
    
class CaracteristicaViewSet(viewsets.ModelViewSet):
    queryset = Caracteristica.objects.all()
    serializer_class = CaracteristicaSerializer