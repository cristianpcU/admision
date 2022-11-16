from django.contrib import admin
from . import models
# Register your models here.
"""
class RespuestaEnLinea(admin.TabularInline):
    model= models.Respuesta
    
class PreguntaAdmin(admin.ModelAdmin):
    enLinea=[RespuestaEnLinea]
"""
#admin.site.register(models.Prueba,models.Categoria)
admin.site.register([models.Evaluacion,models.Pregunta])
#admin.site.register(models.Respuesta,models.Evaluacion)
