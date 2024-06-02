from django.urls import path
from . import views
from django.contrib import admin
app_name = 'presupuesto'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('crearPresupuesto/', views.crearPresupuesto_View, name='crearPresupuesto'),
    path('mostrarPresupuestos/', views.mostrarPresupuesto_View, name='mostrarPresupuestos'),
    path('gestionarCostos/', views.gestionarCostos_View, name='gestionarCostos'),
    path('admin/', admin.site.urls),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.cerrarSesion_view, name='logout'),
    path('signin/', views.inicioSesion_view, name='signin'),
]