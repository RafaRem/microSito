from django.db import models
class Informe(models.Model):
    nombre = models.CharField(max_length=500) 
    año = models.CharField(max_length=500) 
    estatus = models.BooleanField(verbose_name=("Estatus"))
    class Meta:
        verbose_name = "informe"
        verbose_name_plural = "informes"
        
    def __str__(self):
        return self.nombre
# Create your models here.
class Eje(models.Model):
    nombre = models.CharField(  max_length=200, verbose_name="Nombre del Eje")
    descripcion = models.TextField(verbose_name=("Descripción"))
    imagen = models.ImageField(verbose_name=("Imagen"))
    informe = models.ForeignKey(Informe,blank=True, null=True, on_delete=models.CASCADE, verbose_name='Informe')
    class Meta:
        verbose_name = "eje"
        verbose_name_plural = "ejes"
        
    def __str__(self):
        return self.nombre

class Subeje(models.Model):
    nombre = models.CharField(  max_length=200, verbose_name="Nombre del Sub-Eje")
    descripcion = models.TextField(verbose_name=("Descripción"))
    eje = models.ForeignKey(Eje,blank=True, null=True, on_delete=models.CASCADE,verbose_name='Eje Principal')
    estatus = models.BooleanField(verbose_name=("Estatus"))
    imagen = models.ImageField(null=True, verbose_name=("Imagen"))
    class Meta:
        verbose_name = "tema"
        verbose_name_plural = "temas"

    def __str__(self):
        return self.nombre

class GaleriaSub(models.Model):
    subeje = models.ForeignKey(Eje,blank=True, null=True, on_delete=models.CASCADE,verbose_name='Sub-Eje')
    imagen = models.ImageField(verbose_name=("Imagen"))
    estatus = models.BooleanField(verbose_name=("Estatus"))
    class Meta:
        verbose_name = "foto"
        verbose_name_plural = "fotos"
        
    def __str__(self):
        return self.subeje.nombre

class Alcance(models.Model):
    nombre = models.CharField(verbose_name="Descripción de alcance",
    max_length=300)
    estatus = models.BooleanField(verbose_name=("Estatus"))
    class Meta:
        verbose_name = "Catálogo de alcance"
        verbose_name = "Catálogo de alcance"
    def __str__(self):
        return self.nombre

class SubBeneficiarios(models.Model):
    """En este modelo se guardan los alcances de beneficiarios de las actividades"""
    alcance = models.ForeignKey(Alcance, on_delete=models.PROTECT)
    subeje = models.ForeignKey(Subeje, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    class Meta:
        unique_together = ['alcance','subeje']
        verbose_name = "Detalle de beneficiarios"
        verbose_name_plural = "Detalles de beneficiarios"
    def __str__(self):
        return self.alcance.nombre

class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=100)
    estatus = models.BooleanField(verbose_name=("Estatus"))
    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medida'
    def __str__(self):
        return self.nombre

class Indicador(models.Model):
    nombre = models.CharField(max_length=500)
    unidadMedida = models.ForeignKey(UnidadMedida, 
    on_delete=models.PROTECT ,blank=True, null=True)
    estatus = models.BooleanField(verbose_name=("Estatus"))
    class Meta:
        verbose_name = 'Indicador de medición'
        verbose_name_plural = 'Indicadoress de medición'
    def __str__(self):
        return self.nombre

class SubIndicador(models.Model):
    """En esta clase se guardan las variables con las cantidades de las actividades"""
    indicador = models.ForeignKey(Indicador, on_delete=models.PROTECT)
    subeje = models.ForeignKey(Subeje, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    class Meta:
        verbose_name='Detalle de indicadores'
        verbose_name_plural = 'Detalles de indicadores'
        unique_together = ['indicador','subeje']
    def __str__(self):
        return self.indicador.nombre
