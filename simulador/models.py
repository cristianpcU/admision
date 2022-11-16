from django.contrib.auth.models import User
from django.db import models

# Create your models here.
DIFICULTAD = (
    (1, 'Facil'),
    (2,'Medio'),
    (3,'Avanzado'),
)

class Evaluacion(models.Model):
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=120)
    preguntas = models.IntegerField()
    tiempo = models.IntegerField()
    score = models.IntegerField(help_text="Requiere un 60%")
    nivel=models.IntegerField(choices=DIFICULTAD)
    def __str__(self) -> str:
        return f"{self.nombre} | {self.tipo}| {str(self.tiempo)}|"

    def get_preguntas(self):
        return self.pregunta_set.all()
        #return Pregunta.objects.all()#filter(evaluacion__pk=self.pk)

class Categoria(models.Model):
    nombre = models.CharField(verbose_name="Categoria",max_length=100)
    definicion = models.TextField(verbose_name="Definición")
    def __str__(self) -> str:
        return str(self.pk)+" | "+self.nombre
    
class Pregunta(models.Model):
    enunciado= models.TextField(default='')
    justificacion=models.TextField(default='')
    evaluacion= models.ForeignKey(Evaluacion,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,on_delete= models.CASCADE)
    creacion=models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.enunciado}"
    
    def get_respuesta(self):
        return self.respuesta_set.all()

class Respuesta(models.Model):
    respuesta=models.CharField(max_length=200)
    correcta=models.BooleanField(default=False)
    pregunta=models.ForeignKey(Pregunta,on_delete= models.CASCADE)   
    
    def __str__(self) -> str:
        return f"{self.pregunta.enunciado} | {self.respuesta} | {self.correcta}"


class Resultados(models.Model):
    prueba= models.ForeignKey(Evaluacion, on_delete= models.CASCADE)
    user=models.ForeignKey(User, on_delete= models.CASCADE)
    score=models.FloatField()
    
    def __str__(self) -> str:
        return f"{self.pk} | {self.prueba} | {self.user}|{self.score}"
    
    