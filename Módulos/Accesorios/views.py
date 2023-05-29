from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class AccesorioView(TemplateView):
    template_name = "accesorio.html"
