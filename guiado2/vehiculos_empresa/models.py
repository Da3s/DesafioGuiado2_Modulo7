from django.db import models

# Create your models here.


class Vehiculo(models.Model):
    patente= models.CharField(max_length=6, primary_key=True)
    marca= models.CharField(max_length=20, null=False, blank=False)
    modelo= models.CharField(max_length=20, null=False, blank=False)
    year= models.IntegerField(null=False, blank=False)
    activo= models.BooleanField(default=True)
    chofer= models.OneToOneField('Chofer', related_name='vehiculo', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.patente} - {self.marca} {self.modelo}'


class Chofer(models.Model):
    rut= models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo= models.BooleanField(default=False)
    creacion_registro= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.rut}'


class RegistroContabilidad(models.Model):
    fecha_compra= models.DateField(null=False, blank=False)
    valor= models.FloatField(null=False, blank= False)
    vehiculo= models.ForeignKey(Vehiculo, related_name='registrocontabilidad', null=False, blank= False, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.fecha_compra} - {self.vehiculo.patente} - {self.valor}'