from django.db import models

# Create your models here.
class Estacion(models.Model):

   nombre = models.CharField(max_length=255)
   kmsPista = models.IntegerField()
   numeroRemontes = models.IntegerField()
   alturaMaxima = models.IntegerField()
   alturaMinima = models.IntegerField()
   imagen = models.CharField(max_length=255, null=True)

   localizacion = models.ForeignKey('Localizacion', on_delete=models.CASCADE)

   def __str__(self):
      return self.nombre

class Localizacion(models.Model):


   mensaje = models.CharField(max_length=255)
   detalles = models.CharField(max_length=255)

   def __str__(self):
      return self.mensaje

class TipoPista(models.Model):

   mensaje = models.CharField(max_length=255)
   detalles = models.CharField(max_length=255)

   def __str__(self):
      return self.mensaje

class EstacionToTipoPista(models.Model):

   numeroPistas = models.IntegerField()

   tipoPista = models.ForeignKey('TipoPista', on_delete=models.CASCADE)
   estacion = models.ForeignKey('Estacion', on_delete=models.CASCADE)

   def __str__(self):
      return "Oui"

class Usuario(models.Model):

   login = models.CharField(max_length=255)
   password = models.CharField(max_length=255)

   def __str__(self):
      return "Oui"

class EstacionToUsuario(models.Model):

   comentario = models.TextField()
   fecha = models.TextField()
   calificacion = models.IntegerField()

   usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
   estacion = models.ForeignKey('Estacion', on_delete=models.CASCADE)

   def __str__(self):
      return "Oui"




