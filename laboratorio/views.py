from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index (request):
    laboratorio = Laboratorio.objects.all()
    contador = request.session.get('contador',0)
    request.session['contador'] = contador + 1 
        
    context = {'laboratorio':laboratorio,'contador': contador}
    
    return render(request, 'tabla.html',context)

def vista (request):
    if request.method=='POST':
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        laboratorio = Laboratorio(nombre = nombre, ciudad = ciudad, pais = pais)
        laboratorio.save()
        return redirect('/')
    else:
        return render(request, 'ingresar.html')
    
def editar(request,pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    
    context= {'laboratorio':laboratorio}
    
    return render(request, 'editar.html',context)

def actualizareditar(request,id):
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        laboratorio = Laboratorio.objects.get(id=id)
        
        laboratorio.nombre = nombre
        laboratorio.ciudad = ciudad
        laboratorio.pais = pais
        laboratorio.save()
        return redirect('/')
    
def eliminar(request,pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method=='POST':
        laboratorio.delete()
        return redirect('/')
    
    context= {'laboratorio':laboratorio}
    
    return render(request, 'eliminar.html',context)
    
    

    

