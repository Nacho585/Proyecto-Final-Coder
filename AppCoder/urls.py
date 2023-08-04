from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('estacion', views.estacion, name='Estacion'),
    path('sensorshampoo', views.sensorshampoo, name='sensorShampoo'),
    path('usuario', views.usuario, name='Usuario'),
    path('estacionFormulario', views.estacionFormulario, name='EstacionFormulario'),
    path('sensorFormulario', views.sensorFormulario, name='SensorFormulario'),
    path('usuarioFormulario', views.usuarioFormulario, name='UsuarioFormulario'),
    path('eliminarEstacion/<estacion_nombre>/', views.eliminarEstacion, name="EliminarEstacion"),
    path('editarEstacion/<estacion_nombre>/', views.editarEstacion, name="EditarEstacion"),
    path('eliminarSensor/<sensor_nombre>/', views.eliminarSensor, name="EliminarSensor"),
    path('editarSensor/<sensor_nombre>/', views.editarSensor, name="EditarSensor"), 
    path('eliminarUsuario/<usuario_nombre>/', views.eliminarUsuario, name="EliminarUsuario"),
    path('editarUsuario/<usuario_nombre>/', views.editarUsuario, name="EditarUsuario"),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),
    path('about', views.about, name='about'),
]