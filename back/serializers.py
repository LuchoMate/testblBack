from django.db.models import fields
from rest_framework import serializers
from .models import Contacto

class contactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'

