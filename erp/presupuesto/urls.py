from django.urls import path
from . import views
app_name = 'presupuesto'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('crearPresupuesto/', views.crearPresupuesto_View, name='crearPresupuesto'),
    path('registro/', views.registro_view, name='registro'),
]