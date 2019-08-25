from rest_framework import serializers
from .models import Installation, Status
from django.db.models import Avg, Count, Min, Sum, Max, Value

class StatusSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    installation_id = serializers.PrimaryKeyRelatedField(queryset=Installation.objects.all(),source='installation.id')

    class Meta:
        model = Status
        fields = ("id", "status", "notes", "date", "installation_id")

class InstallationSerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=True)
    
    class Meta:
        model = Installation
        fields = ("customer_name", "address", "appointment_date", "date_created", "date_modified",'status')

