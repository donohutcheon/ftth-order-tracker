from django.test import TestCase
from django.utils import timezone
from datetime import datetime

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Installation, Status
from .serializers import InstallationSerializer, StatusSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_installation(customer_name="", address="", appointment_date=""):
        if customer_name != "" and address != "":
            if appointment_date == "":
                appointment_date = timezone.now()
            Installation.objects.create(customer_name=customer_name, address=address, appointment_date=appointment_date)
            
    @staticmethod
    def create_status(status, notes, date, installation):
        if status != "" and notes != "" and date != "" and installation != "":
            Status.objects.create(status=status, notes=notes, date=date, installation=installation)

    def setUp(self):
        self.create_installation("Joe", "13 Elm street", timezone.now())
        self.create_installation("Bob", "1 Oak ave",  timezone.now())
        self.create_installation("Mary", "1st street",  timezone.now())
        self.create_installation("Anne", "26 Main road",  timezone.now())
        installation_set = Installation.objects.all()
        for installation in installation_set:
            self.create_status("REQUESTED", "None", timezone.now(), installation)
            

class GetAllInstallationsTest(BaseViewTest):

    def test_get_all_installations(self):
        response = self.client.get(reverse("installations-all"))
        expected = Installation.objects.all()
        serialized = InstallationSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
