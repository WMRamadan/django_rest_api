from rest_framework import serializers
from .models import shipment

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = shipment
        fields = ('id', 'description', 'from_location', 'to_location', 'date_shipped', 'date_arrived')