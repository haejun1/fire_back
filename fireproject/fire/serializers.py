from rest_framework import serializers
from .models import *

class FireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fire
        fields ='__all__'