from django.contrib import admin
from .models import *

# Register your models here.
class InformeAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

admin.site.register(Informe,InformeAdmin)

class EjeAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

admin.site.register(Eje,EjeAdmin)





class GaleriaAdmin(admin.ModelAdmin):
    list_display=['id', 'subeje', 'especial']
    list_display_links=['id']
    

admin.site.register(GaleriaSub,GaleriaAdmin)


class PublicacionAdmin(admin.ModelAdmin):
    list_display=['id','titulo', 'eje']
    list_display_links=['id','titulo']
    search_fields=['titulo']

admin.site.register(Publicacion,PublicacionAdmin)

class PublicacionEspecialAdmin(admin.ModelAdmin):
    list_display=['id','titulo']
    list_display_links=['id','titulo']
    search_fields=['titulo']

admin.site.register(PublicacionEspecial,PublicacionEspecialAdmin)

class EspecialAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

class VisoresAdmin(admin.ModelAdmin):
    list_display=['id','titulo']
    list_display_links=['id','titulo']
    search_fields=['titulo']

admin.site.register(Visores,VisoresAdmin)

admin.site.register(Especial,EspecialAdmin)