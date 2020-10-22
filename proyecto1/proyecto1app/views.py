from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    return render(request,"proyecto1app/inicio.html")

def Tienda(request):
    return render(request,"proyecto1app/tienda.html")

def Blog(request):
    return render(request,"proyecto1app/blog.html")

def Contacto(request):
    return render(request,"proyecto1app/contacto.html")
