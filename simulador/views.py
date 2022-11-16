from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from . import models
#Listado de evaluaciones
class ListEvaluaciones(ListView):
    model=models.Evaluacion
    template_name="tests/main.html"
    

# Create your views here.
def index(request):
    return render(request, 'index.html')

def examenes(request,id):
    print(id)
    data={}
    evaluaciones=models.Evaluacion.objects.get(pk=id)
    data['evaluaciones']=evaluaciones
    preguntas=[]
    print("PREGUNTAS:",evaluaciones.get_preguntas())
    for p in evaluaciones.get_preguntas():
        respuestas=[]
        for r in p.get_respuesta():
            respuestas.append(r.respuesta)
        
        #preguntas.append({str(p):respuestas})
        preguntas.append({str(p.enunciado):respuestas})
    #print(models.Pregunta.objects.filter(evaluacion=evaluaciones))    
    data['preguntas']=evaluaciones.get_preguntas()
    return render(request,'tests/evaluaciones.html',data)

def preguntas(request):
    return render(request, 'simulador/preguntas.html')