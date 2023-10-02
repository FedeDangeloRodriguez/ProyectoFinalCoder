from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Torneo(models.Model):

    nombre= models.CharField(max_length=30)
    cantidad_equipos= models.IntegerField()
    premio= models.CharField(max_length=30)
    fecha_comienzo= models.DateField()
    imagen= models.ImageField(upload_to='torneos',null=True,blank=True)
    
    class Meta():
        verbose_name= "Tournament"
        verbose_name_plural= "Tournaments"

    def __str__(self):
        return f"{self.nombre}"

class Equipo(models.Model):

    nombre= models.CharField(max_length=30)
    barrio= models.CharField(max_length=30)
    titulos= models.IntegerField()
    division= models.CharField(max_length=10)
    torneo = models.ManyToManyField(Torneo,blank=True)
    imagen= models.ImageField(upload_to='equipos',null=True,blank=True)

    class Meta():
        verbose_name= "Team"
        verbose_name_plural= "Teams"
    
    def __str__(self):
        return f"{self.nombre}"

class Jugador(models.Model):
    
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField()
    equipo= models.ForeignKey(Equipo,on_delete=models.CASCADE)
    posicion= models.CharField(max_length=2)
    imagen= models.ImageField(upload_to='jugadores',null=True,blank=True)

    class Meta():
        verbose_name= "Player"
        verbose_name_plural= "Players"

    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.equipo}"

class Entrenador(models.Model):
        
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField()
    equipo= models.ForeignKey(Equipo,on_delete=models.CASCADE)
    titulos= models.IntegerField()
    imagen= models.ImageField(upload_to='entrenadores',null=True,blank=True)

    class Meta():
        verbose_name= "Coach"
        verbose_name_plural= "Coaches"

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)

