import os
from core.models import Eje
from django.conf import settings

def add_variable_context(request):
    ejesInforme = Eje.objects.filter(estatus=True) 
    return{
        'settings': settings,
        'ejesInforme': ejesInforme
    }