from django.shortcuts import render
from rest_framework import generics
from .models import Installation, Status
from .serializers import InstallationSerializer, StatusSerializer

class ListInstallationsView(generics.ListAPIView):
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer

class CreateInstallationView(generics.CreateAPIView):
    serializer_class = InstallationSerializer


