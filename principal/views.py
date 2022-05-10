from django.shortcuts import render
from .models import Departamento

def inicio(request):
    Departamentos = Departamento.objects.all()
    contexto = {
        'Departamentos':Departamentos
    }
    return render(request, 'index.html', contexto)
