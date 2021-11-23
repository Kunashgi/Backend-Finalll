from rest_framework import serializers
from Data.models import Code, Reserva, Users, Cancelacion, Contact

class ReservaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reserva
    fields = ('email', 'name', 'comuna', 'direccion', 'phone', 'marca', 'año', 'modelo', 'problema', 'fecha', 'hora', 'ID')

class UsersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Users
    fields = ('name', 'email', 'phone', 'password', 'passwordconfirm', 'code', 'ID')

class CancelacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cancelacion
    fields = ('email', 'code', 'descripcionCancelacion', 'ID')

class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = ('name', 'email', 'phone', 'mensaje', 'ID')

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
      model = Code
      fields = ('code', 'ID')