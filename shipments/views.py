# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from .models import shipment
from .serializers import ShipmentSerializer

class ShipmentView(viewsets.ModelViewSet):
    queryset = shipment.objects.all()
    serializer_class = ShipmentSerializer
