from django.urls import path , include
from Login import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
path('login', views.login_request, name = 'signup'),
path('register', views.register, name='Register'),
path('logout', LogoutView.as_view(template_name='Login/logout.html'), name='Logout'),
path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
]