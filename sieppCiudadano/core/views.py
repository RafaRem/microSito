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
        covid = False
        informes = Informe.objects.filter(estatus = True )
        inf = Informe.objects.filter(año = inf)
        if len(inf) == 0:
            url = reverse('inicio')
            return redirect(url)
        
        inf = inf[0]
        galeria = GaleriaInf.objects.filter(informe= inf)
        print(inf)
        ejes = Eje.objects.filter(informe = inf, estatus = True)
        ejes = ejes.order_by('numero')
        ordenar = []
        for ed in ejes:
            if ed.numero != "2":
                ordenar.append(ed)
            else:
                covid = ed
        if covid:
            ordenar.append(covid)
        ejes = ordenar
        fecha_inf = inf.año
        return  render(request, "inicio.html",{
        'informe': True,
        'icono': inf.imagen,    
        'galeria': galeria,
        'informes': informes,
        'eje': inf,
        'ejes': ejes,
        'descripcion':False,
        'fecha':fecha_inf
        
        
        })

       
    def post(self,request,idIndicador=0):
        return  render(request, "inicio.html",{'notas': 'notas'})

class InicioInformes(View):
    def get(self,request,):
        fecha = date.today()
        inf = Informe.objects.filter(año= fecha.year)
        galeria = GaleriaInf.objects.filter(informe= inf)
        if len(inf) > 0:
            inf = inf[0]
            fecha_informe = str(inf.año)
            url = reverse('informe', args=[str(fecha_informe)])
            return redirect(url)
        
        informes = Informe.objects.filter(estatus=True)
        return  render(request, "inicioInformes.html",{
            'informes': informes
        })




class EjeView(View):
    def get(self,request, idEje='0', fecha=''):
        array=[]
        covid = False
        if not idEje.isnumeric():
            url = reverse('inicio')
            return redirect(url)
        inf = Informe.objects.filter(año = fecha)
        if len(inf) == 0:
            url = reverse('inicio')
            return redirect(url)
        
        inf = inf[0]
        eje = Eje.objects.filter(numero = idEje, informe=inf )
        if len(eje) == 0:
            url = reverse('inicio')
            return redirect(url)
        eje = eje[0]
        galeria = GaleriaSub.objects.filter(subeje = eje)
        publicaciones = Publicacion.objects.filter(eje = eje)
        informes = Informe.objects.filter(estatus = True )
        ejes = Eje.objects.filter(informe = inf, estatus = True)
        ejes = ejes.order_by('numero')
        ordenar = []
        for ed in ejes:
            if ed.numero != "2":
                ordenar.append(ed)
            else:
                covid = ed
        if covid:
            ordenar.append(covid)
        ejes = ordenar
        visores = Visores.objects.filter(estatus=True, eje=eje)
        visores = visores.order_by('-pk')
        arrayvisores= []
        for visor in visores:
            arrayvisores.append({
                'eje': eje.numero,
                'titulo': visor.titulo,
                'mapa': visor.mapa,
                'icono': visor.icono,
                'color': visor.color
        }) 
        fecha_inf = inf.año
        arrayvisores = json.dumps(arrayvisores)
        return  render(request, "inicio.html",{
        'ejes': ejes,
        'eje': eje,
        'id': idEje,
        'galeria': galeria,
        'temas':publicaciones,
        'descripcion':True,
        'informes': informes,
        'visores' : arrayvisores,
        'fecha':fecha,
        'icono': inf.imagen, 
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
        