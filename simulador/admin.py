from django.contrib import admin
from .models import *
# Register your models here.

class RespuestaEnLinea(admin.TabularInline):
    model= Respuesta

class Respuestas(admin.TabularInline):
    model= Respuesta   
class RespuestasAdmin(admin.ModelAdmin):
    #list_display= ('nombre','tipo','tiempo')
    inlines= [Respuestas]
    #enLinea=[RespuestaEnLinea]
admin.site.register([Periodo,Cuestionario,Categoria,Intento, DetalleIntento,Resultados])    
admin.site.register(Pregunta,RespuestasAdmin)