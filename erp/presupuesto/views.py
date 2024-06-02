from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db  import IntegrityError
from .forms import PresupuestoForm
from .models import Presupuesto
from .forms import CostoForm

def home_view(request):
    return render(request, 'home.html')

def crearPresupuesto_View(request):
    if request.method == 'GET':
             return render(request, 'crearpresupuesto.html',{
         'form': PresupuestoForm} )
    else:
             form = PresupuestoForm(request.POST)
             new_Presupuesto = form.save(commit=False)
             new_Presupuesto.save()
             print(new_Presupuesto)
             return redirect('gestionarCostos/')
    
def editarPresupuesto(request, presupuesto_id):
     
     if request.method == 'GET':
      presupuesto=get_object_or_404(Presupuesto,pk=presupuesto_id)
      form=PresupuestoForm(instance=presupuesto)
      return render(request,'editarPresupuesto.html',{'presupuesto':presupuesto, 'form':form})    
     else:
          try:
               presupuesto=get_object_or_404(Presupuesto,pk=presupuesto_id)
               form=PresupuestoForm(request.POST,instance=presupuesto)
               form.save()
               return redirect('/mostrarPresupuestos')
          
          except ValueError:
               return render(request,'editarPresupuesto.html',{'presupuesto':presupuesto, 'form':form , 'error':"Se a producido un error"})
               
def eliminarPresupuesto(request,presupuesto_id):
     
    presupuesto=get_object_or_404(Presupuesto,pk=presupuesto_id)
    
    if request.method =='POST':
         presupuesto.delete()
         return redirect('/mostrarPresupuestos')
          
def agregarCosto_View(request, presupuesto):
     
     if request.method == 'GET':
             
        return render (request,'costo.html',{
        'form': CostoForm     
     } )   

     else :
        try:
            presupuesto=get_object_or_404(Presupuesto,pk=presupuesto)
            form =CostoForm(request.POST)
            newCosto = form.save(commit=False) 
            newCosto.presupuesto = presupuesto
            newCosto.save()
            return redirect('/gestionarCostos')
        except ValueError:
            return render (request,'costo.html',{
            'form': CostoForm,
            'error': 'dato invalido'     
     } )   
             


def mostrarPresupuesto_View(request):
     presupuestos=Presupuesto.objects.all()
     return render(request,'mostrarPresupuestos.html',{'presupuestos':presupuestos})

def gestionarCostos_View(request)  : 
        presupuestos=Presupuesto.objects.all()
        return render(request,'gestionarCostos.html',{'presupuestos':presupuestos})


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