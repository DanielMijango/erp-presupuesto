from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db  import IntegrityError

def home_view(request):
    return render(request, 'home.html')

def crearPresupuesto_View(request):
    return render(request, 'crearpresupuesto.html')

def mostrarPresupuesto_View(request):
     return render(request,'mostrar-presupuestos.html')

def registro_view(request): 
    if request.method == 'GET':
            return render(request, 'registro.html',{
        'form':UserCreationForm
    } )
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #registrar usuario
                user = User.objects.create_user(
                     username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError:
                 return render(request, 'registro.html',{
                    'form':UserCreationForm, 
                    "error": 'el usuario ya existe'
    } )          
    return render(request, 'registro.html',{
                    'form':UserCreationForm, 
                    "error": 'contrasenias no coinciden'                   
} )


def cerrarSesion_view (request):
    logout(request)
    return  redirect('/')

def inicioSesion_view(request):
    if request.method == 'GET':
          return render(request,'iniciosesion.html',{
            'form': AuthenticationForm 
    })
    else:
        user = authenticate (request, username=request.POST['username'], password=request.POST['password'] )  
        if user is None:

            return render(request,'iniciosesion.html',{
            'form': AuthenticationForm,
             'error' : 'nombre o contra invalidos'
              })
        else:
             login(request, user)
             return redirect('mostrarPresupuestos/')