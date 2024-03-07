from django.db import models
from django.conf import settings

# Create your models here.

class PatientRecord(models.Model):
    record_owner = models.ForeignKey(settings.AUTH_USER_MODEL, default='', on_delete=models.CASCADE)
    medical_condition = models.CharField(max_length=50)
    allergies = models.CharField(max_length=70,  null=True, blank=True)
    current_medication = models.CharField(max_length=150,  null=True, blank=True)
    lab_test = models.CharField(max_length=100,  null=True, blank=True)
    test_result = models.CharField(max_length=100,  null=True, blank=True)
    prescription = models.TextField(max_length=250, null=True, blank=True)
    new_appointment = models.DateField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    referral = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return (
                f'Name: {self.record_owner.first_name} {self.record_owner.last_name}'
                f' - Condition: {self.medical_condition}'                
                )
