from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError


def home_view(request):
    return render(request, 'home.html')

def crearPresupuesto_View(request):
    return render(request, 'crearpresupuesto.html')

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
                return redirect('mostrarPresupuestos/')
            except IntegrityError:
                 return render(request, 'registro.html',{
                    'form':UserCreationForm, 
                    "error": 'el usuario ya existe'
    } )          
    return render(request, 'registro.html',{
                    'form':UserCreationForm, 
                    "error": 'contrasenias no coinciden'
} )


def mostrarPresupuestos_view(request):   
    return render(request, 'mostrarPresupuestos.html')
