from rest_framework import serializers
from studentApi.models import Studentmodel,Marksmodel


class Marksserializer(serializers.ModelSerializer):
    class Meta:
        model=Marksmodel
        fields='__all__'

class Studentserializer(serializers.ModelSerializer):
    marks=Marksserializer(read_only=True,many=True)
    class Meta:
        model=Studentmodel
        fields='__all__'