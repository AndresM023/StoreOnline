from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class LoginView(TemplateView):
    template_name = 'login.html'

class RegistroView(TemplateView):
    template_name = 'registro.html'

class ForgetPassword(TemplateView):
    template_name = 'olvidar_clave.html'

class CambiarPassword(TemplateView):
    template_name = 'cambiar_clave.html'
