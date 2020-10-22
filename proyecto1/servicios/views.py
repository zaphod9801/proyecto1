from django.shortcuts import render
from servicios.models import servicio

# Create your views here.

def Servicios(request):
    ser = servicio.objects.all()
    
    contexto ={
        "servicios" : ser
    }
    
    return render(request,"servicios/servicios.html",contexto)