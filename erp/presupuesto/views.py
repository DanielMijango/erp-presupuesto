from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'home.html')

def crearPresupuesto_View(request):
    return render(request, 'crearpresupuesto.html')


