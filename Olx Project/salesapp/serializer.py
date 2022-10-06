

from rest_framework import serializers
from salesapp.models import Vehicles

class VehicleSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)  # ( to show id in output 'read only' )
    class Meta:
        model=Vehicles
        fields="__all__"