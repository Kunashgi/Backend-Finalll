from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Users(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  phone = models.CharField(max_length=12)
  password = models.CharField(max_length=16)
  passwordconfirm = models.CharField(max_length=16)
  code = models.CharField(max_length=20)
  ID = models.AutoField(primary_key=True)

class Reserva(models.Model):
  email = models.EmailField()
  name = models.CharField(max_length = 50)
  comuna = models.CharField(max_length = 30)
  direccion = models.CharField(max_length=100)
  phone = models.CharField(max_length=12)
  marca = models.CharField(max_length=20)
  año = models.IntegerField()
  modelo = models.CharField(max_length=20)
  problema = models.CharField(max_length=500)
  fecha = models.DateField()
  hora = models.CharField(max_length=5)
  ID = models.AutoField(primary_key=True)

class Cancelacion(models.Model):
  email = models.EmailField()
  code = IntegerField(null=True)
  descripcionCancelacion = models.CharField(max_length=500, null=True)
  ID = models.AutoField(primary_key=True)
  
class Contact(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(null=True)
  phone = models.CharField(max_length=12, null=True)
  mensaje = models.CharField(max_length = 500)
  ID = models.AutoField(primary_key=True)