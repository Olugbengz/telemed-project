from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import TeleMedUser, Doctor, DoctorProfile, Patient, PatientProfile


@receiver(post_save, sender=Doctor)
def create_doctor_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'DOCTOR':
        DoctorProfile.objects.create(doctor=instance)


@receiver(post_save, sender=Patient)
def create_patient_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'PATIENT':
        PatientProfile.objects.create(patient=instance)