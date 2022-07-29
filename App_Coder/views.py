from django.http import HttpResponse
from django.shortcuts import render
from App_Coder.forms import CursoFormulario

from App_Coder.models import Curso



# Create your views here.

def curso(self, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado </p>
    
    
    
    """)

def lista_curso(self):

    lista = Curso.objects.all()

    return render(self, "lista_cursos.html" ,{"lista_cursos": lista})


def inicio(self):
    return render(self, "inicio.html")
    

def estudiante(self):
    return render(self, "estudiantes.html")

def profesores(self):
    return render(self, "profesores.html")

def cursos(self):
    return render(self, "cursos.html")

def entregables(self):
    return render(self, "entregables.html")




# def cursoFormulario(request):
#     print('method:', request.method)
#     print('post:', request.POST)

#     if request.method == 'POST':

#         curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
#         curso.save()

#         return render(request, 'inicio.html')

#     return render(request, "cursoFormulario.html")

def cursoFormulario(request):
    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':
        
        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data  #guarda datos en la basededatos

        curso = Curso(nombre=data['curso'], camada=data['camada'])
        curso.save()
        return render(request, 'inicio.html')

    else:
        miFormulario = CursoFormulario()


    return render(request, "cursoFormulario.html", {"miFormulario": miFormulario})


def busquedaCamada(request):

    return render(request, 'busquedaCamada.html')

def buscar(request):

    return HttpResponse(f'Estoy buscando la camada: {request.GET["camada"]}')