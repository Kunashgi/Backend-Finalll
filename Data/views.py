from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Data.models import Reserva, Users, Cancelacion
from Data.serializers import ReservaSerializer, UsersSerializer, CancelacionSerializer

# Create your views here.

@csrf_exempt
def reservaApi(request, id=0):
  if request.method == 'GET':
    reserva = Reserva.objects.all()
    reserva_serializer = ReservaSerializer(reserva, many=True)
    return JsonResponse(reserva_serializer.data, safe=False)

  elif request.method=='POST':
    reserva_data=JSONParser().parse(request)
    reserva_serializer = ReservaSerializer(data=reserva_data)
    if reserva_serializer.is_valid():
      reserva_serializer.save()
      return JsonResponse("agregado con exito,", safe=False)
    return JsonResponse("failed to Add",safe=False)

  elif request.method=='DELETE':
    reserva=Reserva.objects.get(ReservaId=id)
    reserva.delete()
    return JsonResponse("delete sucessfull", safe=False)

@csrf_exempt
def usersApi(request, id=0):
  if request.method == 'GET':
    users = Users.objects.all()
    users_serializer = UsersSerializer(users, many=True)
    return JsonResponse(users_serializer.data, safe=False)

  elif request.method=='POST':
    users_data=JSONParser().parse(request)
    users_serializer = UsersSerializer(data=users_data)
    if users_serializer.is_valid():
      users_serializer.save()
      return JsonResponse("agregado con exito,", safe=False)
    return JsonResponse("failed to Add",safe=False)

  elif request.method=='PUT':
    users_data = JSONParser().parse(request)
    users = Users.objects.get(ID=users_data['ID'])
    users_serializer = UsersSerializer(users,data=users_data)
    if users_serializer.is_valid():
      users_serializer.save()
      return JsonResponse("Update succesfull", safe=False)
    return JsonResponse ("failed update," ,safe=False)

  elif request.method=='DELETE':
    users=Users.objects.get(ID=id)
    users.delete()
    return JsonResponse("delete sucessfull", safe=False)

@csrf_exempt
def cancelacionApi(request, id=0):
  if request.method == 'GET':
    cancelacion = Cancelacion.objects.all()
    cancelacion_serializer = CancelacionSerializer(cancelacion, many=True)
    return JsonResponse(cancelacion_serializer.data, safe=False)

  elif request.method=='POST':
    cancelacion_data=JSONParser().parse(request)
    cancelacion_serializer = CancelacionSerializer(data=cancelacion_data)
    if cancelacion_serializer.is_valid():
      cancelacion_serializer.save()
      return JsonResponse("agregado con exito,", safe=False)
    return JsonResponse("failed to Add",safe=False)