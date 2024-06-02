from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db  import IntegrityError
from.forms import PresupuestoForm

def home_view(request):
    return render(request, 'home.html')

def crearPresupuesto_View(request):
    if request.method == 'GET':
             return render(request, 'crearpresupuesto.html',{
         'form': PresupuestoForm} )
    else:
             form = PresupuestoForm(request.POST)
             new_Presupuesto = form.save(commit=False)
             new_Presupuesto.user = request.user
             new_Presupuesto.save()

             return redirect('gestionarCostos/')

def mostrarPresupuesto_View(request):
     return render(request,'mostrarPresupuestos.html')

def gestionarCostos_View(request)  : 
       return render(request,'gestionarCostos.html')

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