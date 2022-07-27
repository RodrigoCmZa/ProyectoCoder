from django.urls import path

from App_Coder.views import curso, cursos, entregables, estudiante, inicio, lista_curso, profesores


urlpatterns = [
    path('curso/<nombre>/<camada>/', curso),
    path('lista-curso/', lista_curso),
    path('', inicio),
    path('cursos/', cursos),
    path('estudiantes/', estudiante),
    path('profesores/', profesores),
    path('entregables/', entregables),
    
]