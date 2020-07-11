from studentApi.models import Marksmodel,Studentmodel
from studentApi.serializers import Studentserializer,Marksserializer
from rest_framework import viewsets
from rest_framework import filters


class Studentapi(viewsets.ModelViewSet):
    queryset=Studentmodel.objects.all()
    serializer_class=Studentserializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Name']
    
    


class Marksapi(viewsets.ModelViewSet):
    queryset=Marksmodel.objects.all()
    for marks in queryset:
        print(marks)
    serializer_class=Marksserializer