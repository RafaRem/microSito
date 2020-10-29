from django.db import models
class Informe(models.Model):
    nombre = models.CharField(max_length=500) 
    año = models.CharField(max_length=500) 
    imagen = models.ImageField(verbose_name=("Imagen") , null=True)
    estatus = models.BooleanField(verbose_name=("Estatus"))
    documento = models.FileField(blank=True, null=True)
    decoracion = models.CharField( max_length=200, null=True, verbose_name="Color Principal del Informe") 
    principal = models.CharField(max_length=500, null=True, verbose_name="Eje que se mostrara primero")
    video = models.FileField(upload_to='uploads/', null= True,blank=True, verbose_name="Video Promocional")
    class Meta:
        verbose_name = "informe"  
        verbose_name_plural = "informes"
        
    def __str__(self):
        return self.nombre

# Create your models here.
class Eje(models.Model):
    nombre = models.CharField(  max_length=200, verbose_name="Nombre del Eje")
    titulo = models.CharField(  max_length=200,null=True, verbose_name="Titulo")
    numero = models.CharField(  max_length=200, verbose_name="Número")
    descripcion = models.TextField(verbose_name=("Descripción"))
    imagen = models.ImageField(verbose_name=("Imagen"))
    informe = models.ForeignKey(Informe,blank=True, null=True, on_delete=models.CASCADE, verbose_name='Informe')
    estatus = models.BooleanField(verbose_name=("Estatus"), default=True)
    documento = models.FileField(blank=True, null=True)
    decoracion = models.CharField( max_length=200, null=True, verbose_name="Color base")
    video = models.FileField(upload_to='uploads/', null= True, blank=True, verbose_name="Video Promocional")
    class Meta:
        verbose_name = "eje"
        verbose_name_plural = "ejes"
        
    def __str__(self):
        return self.nombre


'''esta clase se debera eliminar'''
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

'''esta clase se debera eliminar'''
class Alcance(models.Model):
    nombre = models.CharField(verbose_name="Descripción de alcance",
    max_length=300)
    estatus = models.BooleanField(verbose_name=("Estatus"))
    class Meta:
        verbose_name = "Catálogo de alcance"
        verbose_name = "Catálogo de alcance"
    def __str__(self):
        return self.nombre
'''esta clase se debera eliminar'''
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
'''esta clase se debera eliminar'''
class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=100)
    estatus = models.BooleanField(verbose_name=("Estatus"))
    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medida'
    def __str__(self):
        return self.nombre
'''esta clase se debera eliminar'''
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
'''esta clase se debera eliminar'''
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


class Publicacion(models.Model):
    titulo = models.CharField(  max_length=200, verbose_name="titulo")
    descripcion = models.TextField(verbose_name=("Descripción"), null=True)
    eje = models.ForeignKey(Eje,blank=True, null=True, on_delete=models.CASCADE,verbose_name='Eje Principal')
    estatus = models.BooleanField(verbose_name=("Estatus"))
    imagen = models.ImageField(null=True, verbose_name=("Imagen"))
    class Meta:
        verbose_name = "publicación"
        verbose_name_plural = "publicaciones"

    def __str__(self):
        return self.titulo

class Especial(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del apartado Especial")
    descripcion = models.TextField(verbose_name=("Descripción"))
    imagen = models.ImageField(verbose_name=("Imagen"))
    informe = models.ForeignKey(Informe,blank=True, null=True, on_delete=models.CASCADE, verbose_name='Informe')
    estatus = models.BooleanField(verbose_name=("Estatus"), default=True)
    video = models.FileField(upload_to='uploads/', null= True, verbose_name="Video Promocional")
    class Meta:
        verbose_name = "Apartado Especial"
        verbose_name_plural = "Apartados Espceciales"
        
    def __str__(self):
        return self.nombre

class PublicacionEspecial(models.Model):
    titulo = models.CharField(  max_length=200, verbose_name="titulo")
    descripcion = models.TextField(verbose_name=("Descripción"), null=True)
    especial = models.ForeignKey(Especial,blank=True, null=True, on_delete=models.CASCADE,verbose_name='Evento Especial')
    estatus = models.BooleanField(verbose_name=("Estatus"))
    imagen = models.ImageField(null=True, verbose_name=("Imagen"))
    class Meta:
        verbose_name = "Publicación especial"
        verbose_name_plural = "Publicaciones Especiales"

    def __str__(self):
        return self.titulo

        
class GaleriaSub(models.Model):
    subeje = models.ForeignKey(Eje,blank=True, null=True, on_delete=models.CASCADE ,verbose_name='Galeria Eje')
    especial = models.ForeignKey(Especial,blank=True, null=True, on_delete=models.CASCADE ,verbose_name='Evento Especial')
    imagen = models.ImageField(verbose_name=("Imagen"))
    estatus = models.BooleanField(verbose_name=("Estatus"))
    class Meta:
        verbose_name = "foto"
        verbose_name_plural = "fotos"
        
    def __str__(self):
        if self.subeje:
            return self.subeje.nombre
        else: 
            return self.especial.nombre

class GaleriaInf(models.Model):
    informe = models.ForeignKey(Informe,blank=True, null=True, on_delete=models.CASCADE, verbose_name='Informe')
    imagen = models.ImageField(verbose_name=("Imagen"))
    estatus = models.BooleanField(verbose_name=("Estatus"))
    class Meta:
        verbose_name = "foto informe"
        verbose_name_plural = "fotos informe"
        
    def __str__(self):
        if self.informe.nombre:
            return self.informe.nombre
        else: 
            return self.informe
            
class Visores(models.Model):
    titulo = models.CharField(max_length=500, verbose_name=("Titulo")) 
    descripcion = models.TextField(verbose_name=("Descripción"))
    eje = models.ForeignKey(Eje,blank=True, null=True, on_delete=models.CASCADE,verbose_name='Eje')
    mapa = models.CharField(max_length=500, verbose_name=("Mapa"))
    link = models.CharField(max_length=800, verbose_name=("Link del Mapa")) 
    icono = models.CharField(max_length=100, null=True, verbose_name=("Icono del bonto"))
    color = models.CharField(max_length=100, null=True, verbose_name=("Color del bonto"))
    estatus = models.BooleanField(verbose_name=("Estatus"))
    class Meta:
        verbose_name = "Visor"  
        verbose_name_plural = "Visores"
        
    def __str__(self):
        return self.titulo
