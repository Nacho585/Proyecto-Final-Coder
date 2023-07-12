from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('estacion', views.estacion, name='Estacion'),
    path('sensorshampoo', views.sensorshampoo, name='sensorShampoo'),
    path('usuario', views.usuario, name='Usuario'),
]