from django.urls import path

from App_Coder.views import buscar, curso, cursoFormulario, cursos, entregables, estudiante, inicio, lista_curso, profesores, busquedaCamada


urlpatterns = [
    path('curso/<nombre>/<camada>/', curso),
    path('lista-curso/', lista_curso),
    path('', inicio,name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiante, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
    path('entregables/', entregables, name="Entregables"),
    path('cursoFormulario/', cursoFormulario, name="CursoFormulario"),
    path('busquedaCamada/', busquedaCamada, name="BusquedaCamada"),
    path('buscar/', buscar, name="Buscar"),
]