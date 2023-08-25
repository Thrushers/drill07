from django.db import models

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, null=True)
    pais = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.nombre
    
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.DO_NOTHING )
    especialidad = models.CharField(max_length=100, null=True)
    
    class Meta:
        verbose_name = 'Director General'
        verbose_name_plural = 'Directores Generales'
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.TextField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.DO_NOTHING )
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nombre
     