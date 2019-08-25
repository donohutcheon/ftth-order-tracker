from django.db import models
from django.utils import timezone

class Installation(models.Model):
    customer_name = models.CharField(max_length=64, null = False)
    address = models.TextField(null = False)
    appointment_date = models.DateTimeField(null = False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "customer_name = {}, address = {}, appointment_date = {}, date_created = {}, date_modified = {}".format(self.customer_name, self.address, self.appointment_date, self.date_created, self.date_modified)
        
    class Meta:
        ordering = ('-appointment_date',)
        get_latest_by = 'date_modified'

class Status(models.Model):
    STATUS_CHOICES = [
        ('REQUESTED', 'Installation requested'),
        ('IN_PROGRESS', 'Installation in progress'),
        ('COMPLETED', 'Installation complete'),
        ('REJECTED', 'Installation rejected'),
    ]

    status = models.CharField(max_length = 16, choices = STATUS_CHOICES, default = 'REQUESTED', null = False)
    notes = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    installation = models.ForeignKey(Installation, on_delete = models.CASCADE, null = False, related_name='status')
    
    def __str__(self):
        return "status : {},  notes : {}, date : {}, installation : {}".format(self.status, self.notes, self.date, self.installation)

    class Meta:
        ordering = ('-date',)
        get_latest_by = 'date'
