from django.contrib import admin
from django.urls import path
from . import views as vista
urlpatterns = [
    path('',vista.ListCuestionario.as_view(), name="evaluaciones"),
    path('test/',vista.preguntas, name="preguntas"),
    path("<id>/", vista.examenes, name="examen")
]