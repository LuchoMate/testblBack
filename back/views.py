from django.shortcuts import render
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Contacto
from .serializers import contactoSerializer

@api_view(['GET'])
def api_getContactos(request):
    contactos = Contacto.objects.all()
    serializer = contactoSerializer(contactos, context={'request': request}, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_crearContacto(request):
    serializer = contactoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def api_actualizarContacto(request, contactoId):
    try:
        contacto = Contacto.objects.get(id=contactoId)
    except Contacto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = contactoSerializer(contacto, data=request.data,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_borrarContacto(request, contactoId):
    try:
        contacto = Contacto.objects.get(id=contactoId)
    except Contacto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    contacto.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
