from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
import json
from . import models
#Listado de evaluaciones
class ListCuestionario(ListView):
    model=models.Cuestionario
    template_name="tests/main.html"
    

# Create your views here.
def index(request):
    return render(request, 'index.html')

def examenes(request,id):
    print(request.method)
    
    if request.method == 'POST':
        print("llegue;", request)
        print("POST:",request.POST)
        cuestionario=request.POST['cuestionario']
        pregunta=request.POST['pregunta']
        respuesa=request.POST['respuesta']
        
        return HttpResponse(json.dumps({"result":True}),content_type='application/json')
    else:
        data={}
        evaluaciones=models.Cuestionario.objects.get(pk=id)
        user=User.objects.get(pk=1)
        
        intento=models.Intento(cuestionario=evaluaciones,user=user)
        #intento.save()
        data['evaluaciones']=evaluaciones
        data['preguntas']=evaluaciones.get_preguntas()
        data['intento']=intento
        return render(request,'tests/evaluaciones.html',data)   
    #preguntas=[]
    #for p in evaluaciones.get_preguntas():
    #    respuestas=[]
     #   for r in p.get_respuesta():
     #       respuestas.append(r.respuesta)    
        #preguntas.append({str(p):respuestas})
    #preguntas.append({str(p.enunciado):respuestas})
    #print(models.Pregunta.objects.filter(evaluacion=evaluaciones))"""    


def preguntas(request):
    return render(request, 'simulador/preguntas.html')