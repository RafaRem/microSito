from django.contrib import admin
from .models import *

# Register your models here.
class InformeAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

class EjeAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

admin.site.register(Eje,EjeAdmin)

class SubejeAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

admin.site.register(Subeje,SubejeAdmin)

class AlcanceAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

admin.site.register(Alcance,AlcanceAdmin)

class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

admin.site.register(UnidadMedida,UnidadMedidaAdmin)

class IndicadorAdmin(admin.ModelAdmin):
    list_display=['id','nombre']
    list_display_links=['id','nombre']
    search_fields=['nombre']

admin.site.register(Indicador,IndicadorAdmin)

class SubBeneficiarioAdmin(admin.ModelAdmin):
    list_display=['id']
    list_display_links=['id']
    

admin.site.register(SubBeneficiarios,SubBeneficiarioAdmin)

class SubIndicadorAdmin(admin.ModelAdmin):
    list_display=['id']
    list_display_links=['id']
    

admin.site.register(SubIndicador,SubIndicadorAdmin)


class GaleriaAdmin(admin.ModelAdmin):
    list_display=['id']
    list_display_links=['id']
    

admin.site.register(GaleriaSub,GaleriaAdmin)


