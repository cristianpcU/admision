from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
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
        print("POST:",request.POST)
        cuestionario=request.POST['cuestionario']
        pregunta=request.POST['pregunta']
        respuesta=request.POST['respuesta']
        punto= models.Respuesta.objects.get(pk=respuesta)
        punto=1 if punto.correcta else 0
        print("puntuacion=",punto) 
        intento=1
        if not models.DetalleIntento.objects.filter(intento_id=intento,pregunta_id=pregunta).exists():
            det = models.DetalleIntento(intento_id=intento,pregunta_id=pregunta,respuesta_id=respuesta,puntuacion=punto)
            det.save()
            print("no existe")
        else:
            det=models.DetalleIntento.objects.get(intento_id=intento,pregunta_id=pregunta)
            det.respuesta_id=respuesta
            det.puntuacion=punto
            det.save()
            print("existe")
            #
        
        return HttpResponse(json.dumps({"result":True}),content_type='application/json')
    else:
        data={}
        if models.Cuestionario.objects.filter(pk=id).exists():
            evaluaciones=models.Cuestionario.objects.get(pk=id)
            user=User.objects.get(pk=1)
            intento=models.Intento(cuestionario=evaluaciones,user=user)
            intento.save()
            data['evaluaciones']=evaluaciones
            data['preguntas']=evaluaciones.get_preguntas()
            data['intento']=intento
            return render(request,'tests/evaluaciones.html',data)   
        else:
            return HttpResponseRedirect('/simulador/')   


def preguntas(request):
    return render(request, 'simulador/preguntas.html')