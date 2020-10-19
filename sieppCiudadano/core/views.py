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
            if int(inf.principal) > 0:
                url = reverse('Eje', args=(inf.principal))
                return redirect(url)
        else:
            inf = Informe.objects.get(año = inf)
        ejes = Eje.objects.filter(informe = inf, estatus = True)
        ejes = ejes.order_by('numero')
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
        if not idEje.isnumeric():
            print("si es")
            return  render(request, "404.html")
        eje = Eje.objects.get(numero = idEje,
        )
        fecha = date.today()
        inf = Informe.objects.get(año= fecha.year)
        galeria = GaleriaSub.objects.filter(subeje = eje)
        publicaciones = Publicacion.objects.filter(eje = eje)
        informes = Informe.objects.filter(estatus = True )
        ejes = Eje.objects.filter(informe = inf, estatus = True)
        ejes = ejes.order_by('numero')
        visores = Visores.objects.filter(estatus=True, eje=eje)
        arrayvisores= []
        for visor in visores:
            arrayvisores.append({
                'titulo': visor.titulo,
                'mapa': visor.mapa,
                'icono': visor.icono,
                'color': visor.color
            }) 
        if eje.numero == '2' and inf.año == '2020':
            
            arrayvisores = json.dumps(arrayvisores)
            return  render(request, "covid.html",{
            'eje': eje,
            'ejes': ejes,
            'temas': publicaciones,
            'id': idEje,
            'galeria': galeria,
            'informes': informes,
            'visores' : arrayvisores
            })


        return  render(request, "inicio.html",{
        'ejes': ejes,
        'eje': eje,
        'id': idEje,
        'galeria': galeria,
        'temas':publicaciones,
        'descripcion':True,
        'informes': informes,
        'visores' : arrayvisores
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
        