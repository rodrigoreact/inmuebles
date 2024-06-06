from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Region(models.Model):
    nombre =models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class Comuna(models.Model):
    nombre=models.CharField(max_length=100)
    region=models.ForeignKey(Region, related_name='comunas', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES=[
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),         
    ]

    nombres= models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    rut = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=100)
    telefono=models.CharField(max_length=13)
    tipo_usuario=models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos}" 

class Inmueble(models.Model):
    TIPO_INMUEBLE_CHOICES=[
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela', 'Parcela'),      
    ]   
    nombre= models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=50)
    imagen= models.ImageField(upload_to='', null=True, blank=True)
    precio= models.DecimalField(max_digits=10, decimal_places=0)
    region=models.ForeignKey(Region, related_name='inmuebles', on_delete=models.CASCADE, default=1)
    comuna= models.ForeignKey(Comuna, related_name='inmuebles', on_delete=models.CASCADE)
    disponible= models.BooleanField(default=False)
    m2_construidos= models.DecimalField(max_digits=10, decimal_places=2)
    m2_terreno= models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_estacionamientos= models.PositiveBigIntegerField()
    cantidad_habitaciones= models.PositiveBigIntegerField()
    cantidad_banos= models.PositiveBigIntegerField()
    tipo_de_inmueble= models.CharField(max_length=12, choices=TIPO_INMUEBLE_CHOICES)
    propietario=models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self)->str:
        return f"{self.nombre}"

class SolicitudArriendo(models.Model):
    TIPO_ESTADO_CHOICES=[
        ('pendiente', 'Pendientye'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),        
    ]
    arrendatario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    mensaje = models.TextField(blank=True)
    estado = models.CharField(choices=TIPO_ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"Solicitud de {self.inmueble.nombre} por {self.arrendatario.nombres} {self.arrendatario.apellidos}"