from django.shortcuts import render
from PaginaWeb.models import Curso
from PaginaWeb.forms import LoginFormulario, BusquedaFormulario

# Create your views here.

def PaginaWeb(request):
    
    return render(request, r"PaginaWeb\PaginaWeb.html")

def crear_login(request):
    
    if request.method == "POST":
        formulario = LoginFormulario(request.POST)     
        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(usuario=data.get('titulo'), contrasenia=data.get("contrasenia"), email=data.get("email"))
            curso = curso
        else:
            return render(request, r"PaginaWeb\crear_login.html", {"formulario":formulario})
        
    formulario = LoginFormulario()
    return render(request, r"PaginaWeb\crear_login.html", {"formulario":formulario})

def busqueda(request):
    formulario = BusquedaFormulario(request.GET)   
      
    if formulario.is_valid():
        usuario_busqueda = formulario.cleaned_data.get("usuario")
        usuario_encontrado = Curso.objects.filter(usuario__icontains=usuario_busqueda)  
    else:
        usuario_encontrado = Curso.objects.all()
        
    formulario = BusquedaFormulario()
    return render(request, r"PaginaWeb\busqueda.html", {"formulario":formulario, "usuario_encontrado":usuario_encontrado})