from django.db import models
"""
Modelo: Caracteristica
Descripción: Representa una característica única identificada por un texto. Este modelo puede ser utilizado
para almacenar descripciones, etiquetas, propiedades u otras entidades con valor textual único.

Autor: Eduardo Vargas Perero
Correo: eduardoevargasp@hotmail.com
Fecha: 2025-06-12
"""
class Caracteristica(models.Model):
    texto = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.texto