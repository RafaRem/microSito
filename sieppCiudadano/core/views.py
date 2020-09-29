import json
from django.shortcuts import render,  redirect,HttpResponse
from django.http import JsonResponse
from .models import *
from django.urls import reverse

from django.views.generic import  View
from datetime import date
from datetime import datetime
from rest_framework.renderers import JSONRenderer

# Create your views here.
  
class notasView(View):
    def get(self,request,inf=0):
        array=[]
        print("entre aqui")
        informes = Informe.objects.filter(estatus = True )
        if inf == 0:

            fecha = date.today()
            inf = Informe.objects.get(año= fecha.year)
            url = reverse('covid')#args=(programaOperativo.id,)
            return redirect(url)

        else:
            inf = Informe.objects.get(año = inf)
        ejes = Eje.objects.filter(informe = inf, estatus = True)
        return  render(request, "inicio.html",{
        'informes': informes,
        'eje': inf,
        'descripcion':False,
        'ejes': ejes
        })

       
    def post(self,request,idIndicador=0):
        return  render(request, "inicio.html",{'notas': 'notas'})

class EjeView(View):
    def get(self,request, idEje):
        array=[]
        eje = Eje.objects.get(pk =idEje,
        )
        galeria = GaleriaSub.objects.filter(subeje = eje)
        publicaciones = Publicacion.objects.filter(eje = eje)
        informes = Informe.objects.filter(estatus = True )
        return  render(request, "inicio.html",{
        'eje': eje,
        'id': idEje,
        'galeria': galeria,
        'temas':publicaciones,
        'descripcion':True,
        'informes': informes
        })

class CovidView(View):
    def get(self,request):
        array=[]
        informes = Informe.objects.filter(estatus = True )
        covid = Especial.objects.get(pk=1)
        publicaciones = PublicacionEspecial.objects.filter(especial = covid) 
        galeria = GaleriaSub.objects.filter(especial = covid)
        visores = Visores.objects.filter(estatus=True)
        arrayvisores= []
        for visor in visores:
            arrayvisores.append({
                'titulo': visor.titulo,
                'mapa': visor.mapa,
                'icono': visor.icono,
                'color': visor.color
            }) 
        arrayvisores = json.dumps(arrayvisores)
        return  render(request, "covid.html",{
            'apartado': covid,
            'publicaciones': publicaciones,
            'galeria': galeria,
            'informes': informes,
            'visores' : arrayvisores
        })
        