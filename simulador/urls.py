from django.contrib import admin
from django.urls import path
from . import views as vista
urlpatterns = [
    path('',vista.ListEvaluaciones.as_view(), name="evaluaciones"),
    path('test/',vista.preguntas, name="preguntas"),
    path("<id>/", vista.examenes, name="examen")
]