from django.contrib import admin

from App_Coder.models import Curso, Entregable, Estudiante, Profesor

# Register your models here.

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'profesion', 'email']
    search_fields = ['nombre', 'apellido']



admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Entregable)


