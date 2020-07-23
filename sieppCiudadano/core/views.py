from django.shortcuts import render, HttpResponse
from .models import *
from django.views.generic import  View

# Create your views here.
  
class notasView(View):
    def get(self,request):
        return  render(request, "inicio.html",{'notas': 'notas'})
    def post(self,request,idIndicador=0):
        return  render(request, "inicio.html",{'notas': 'notas'})

class EjeView(View):
    def get(self,request, idEje):
        array=[]
        eje = Eje.objects.get(pk =idEje)
        galeria = GaleriaSub.objects.filter(subeje = eje)
        temas = Subeje.objects.filter(eje = eje)
        for tema in temas:
            if tema.imagen:
                print("entro")
                array.append(tema)
        print(temas)
        return  render(request, "inicio.html",{
        'eje': eje,
        'id': idEje,
        'galeria': galeria,
        'temas':array
        })
        