from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
import random
# Create your models here.
DIFICULTAD = (
    (1, 'Facil'),
    (2,'Medio'),
    (3,'Avanzado'),
)

class Periodo(models.Model):
    nombre = models.CharField(default='', max_length=200, verbose_name=u'Nombre')
    alias = models.CharField(default='', max_length=200, verbose_name=u'Nombre')
    inicio = models.DateField(verbose_name=u'Fecha inicio')
    fin = models.DateField(verbose_name=u'Fecha fin')
    activo = models.BooleanField(default=True, verbose_name=u'Visible')
    def __str__(self) -> str:
        return self.nombre
class Cuestionario(models.Model):
    periodo=models.ForeignKey(Periodo, verbose_name='Periodo' , on_delete=models.CASCADE)
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=120)
    preguntas = models.IntegerField()
    fecha= models.DateTimeField( default=datetime.now)
    tiempo = models.TimeField()
    score = models.IntegerField(help_text="Requiere un 60%")
    nivel=models.IntegerField(choices=DIFICULTAD)
    def __str__(self) -> str:
        return f"{self.nombre} | {self.tipo}| {str(self.tiempo)}|"

    def get_preguntas(self):
        preguntas=list(self.pregunta_set.all())
        #Ordena al azar
        random.shuffle(preguntas)
        return preguntas[:self.preguntas]
        #return Pregunta.objects.all()#filter(evaluacion__pk=self.pk)
    
class Categoria(models.Model):
    nombre = models.CharField(verbose_name="Categoria",max_length=100)
    definicion = models.TextField(verbose_name="Definición")
    def __str__(self) -> str:
        return str(self.pk)+" | "+self.nombre
    
class Pregunta(models.Model):
    enunciado= models.TextField(default='')
    justificacion=models.TextField(default='')
    cuestionario= models.ForeignKey(Cuestionario,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,on_delete= models.CASCADE)
    creacion=models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.enunciado}"
    
    def get_respuesta(self):
        respuestas=list(self.respuesta_set.all())
        random.shuffle(respuestas)
        return respuestas

class Respuesta(models.Model):
    respuesta=models.CharField(max_length=200)
    correcta=models.BooleanField(default=False)
    pregunta=models.ForeignKey(Pregunta,on_delete= models.CASCADE)   
    
    def __str__(self) -> str:
        return f"{self.pregunta.enunciado} | {self.respuesta} | {self.correcta}"
    def es_correcta(self):
        return self.correcta

class Intento(models.Model):
    cuestionario=models.ForeignKey(Cuestionario, on_delete= models.CASCADE)
    user=models.ForeignKey(User, on_delete= models.CASCADE)
    score=models.FloatField(default=0)
    fecha=models.DateTimeField(auto_now_add=True)
    
class DetalleIntento(models.Model):
    intento=models.ForeignKey(Intento, on_delete= models.CASCADE)
    pregunta=models.ForeignKey(Pregunta,on_delete= models.CASCADE)
    respuesta=models.ForeignKey(Respuesta,on_delete=models.CASCADE)
    puntuacion=models.IntegerField(default=0)
        
class Resultados(models.Model):
    cuestionario= models.ForeignKey(Cuestionario, on_delete= models.CASCADE)
    user=models.ForeignKey(User, on_delete= models.CASCADE)
    score=models.FloatField()
    
    def __str__(self) -> str:
        return f"{self.pk} | {self.prueba} | {self.user}|{self.score}"
    
    