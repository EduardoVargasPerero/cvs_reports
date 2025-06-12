from rest_framework import serializers
from .models import Caracteristica

"""
Serializers para el manejo de carga de archivos PDF y del modelo Caracteristica.

Autor: Eduardo Vargas Perero
Correo: eduardoevargasp@hotmail.com
Fecha: 2025-06-12
"""
class PDFUploadSerializer(serializers.Serializer):
    archivos = serializers.ListField(
        child=serializers.FileField(),
        allow_empty=False
    )

    # def validate_archivos(self, archivos):
    #     errores = []
    #     for archivo in archivos:
    #         if archivo.content_type != 'application/pdf':
    #             errores.append(archivo.name)
    #     if errores:
    #         raise serializers.ValidationError(f"Los siguientes archivos no son PDF: {', '.join(errores)}")
    #     return archivos
    
    
class CaracteristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristica
        fields = '__all__'

    def validate_texto(self, value):
        return value.upper()