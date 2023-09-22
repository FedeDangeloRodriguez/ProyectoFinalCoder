from django.db import models

# Create your models here.

class Torneo(models.Model):

    nombre= models.CharField(max_length=30)
    cantidad_equipos= models.IntegerField()
    premio= models.CharField(max_length=30)
    fecha_comienzo= models.DateField()

    def __str__(self):
        return f"{self.nombre}"

class Equipo(models.Model):

    nombre= models.CharField(max_length=30)
    barrio= models.CharField(max_length=30)
    titulos= models.IntegerField()
    division= models.CharField(max_length=10)
    torneo = models.ManyToManyField(Torneo,blank=True)

    def __str__(self):
        return f"{self.nombre}"

class Jugador(models.Model):
    
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField()
    equipo= models.ForeignKey(Equipo,on_delete=models.CASCADE, null=False,blank=False)
    posicion= models.CharField(max_length=2)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Entrenador(models.Model):
        
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField()
    equipo= models.ForeignKey(Equipo,on_delete=models.CASCADE, null=False,blank=False)
    titulos= models.IntegerField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


