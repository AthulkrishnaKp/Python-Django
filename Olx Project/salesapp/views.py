from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ViewSet
from salesapp.serializer import VehicleSerializer
from salesapp.models import Vehicles

class VehicleModelViewsetView(ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicles.objects.all()
