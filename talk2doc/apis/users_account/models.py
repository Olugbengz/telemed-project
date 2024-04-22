from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from .managers import CustomUserManager
from apis.patient_record.models import PatientRecord

# Create your models here.



class TeleMedUser(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        DOCTOR = "DOCTOR", "Doctor"
        PATIENT = "PATIENT", "Patient"
   
    base_role = Role.ADMIN
    username = None
    email = models.EmailField(unique=True, verbose_name='email address', max_length=255)
    first_name = models.CharField(max_length=20, null=True, blank=True, )
    last_name = models.CharField(max_length=20, null=True, blank=True, )    
    phone = models.CharField(max_length=20, null=True, blank=True, )
    role = models.CharField(max_length=20, choices=Role.choices, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/')
    is_staff = models.BooleanField(default=False, null=True, blank=True, )
    is_active = models.BooleanField(default=False, null=True, blank=True, )
    is_admin = models.BooleanField(default=False, null=True, blank=True, )
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True, )
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True, )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']
    

    objects = CustomUserManager()

    

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def fullname(self):
        return '%s %s' % (self.first_name, self.last_name)



class DoctorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=TeleMedUser.Role.DOCTOR)


class Doctor(TeleMedUser):
    base_role = TeleMedUser.Role.DOCTOR

    doctor = DoctorManager()

    class Meta:
        proxy = True


   

class DoctorProfile(models.Model):
    DOC_SPECIALTY = [
        ('INTERNAL MEDICINE', 'Internal Medicine'),
        ('PEDIATRICIAN', 'Pediatrician'),
        ('ORTHOPEDIST', 'Orthopedist'),
        ('PSYCHIATRIST', 'Psychiatrist'),
        ('UROLOGIST', 'Urologist'),
        ('PATHOLOGIST', 'Pathologist'),
        ('NEUROLOGIST', 'Neurologist'),
        ('GASTROENTEROLOGIST', 'Gastroenterologist'),
        ('ANESTHESIOLOGIST', 'Anesthesiologist'),
        ('OBSTERICIAN', 'Obsterician'),
        ('GYNAECOLOGIST', 'Gynaecologist'),
        ('DERMATOLOGIST', 'Dermatologist'),
        ('RHEUMATOLOGIST', 'Rheumatologist'),
        ('OPHTHALMOLOGIST', 'Ophthalmologist'),
        ('CARDIOLOGIST', 'Cardiologist'),
        ('FAMILY MEDICINE', 'Family Medicine'),
        ('RADIOLOGIST', 'Radiologist'),
        ('NEUROLOGIST', 'Neurologist'),
        ('ONCOLOGIST', 'Oncologist'),
        ('NEPHEROLOGIST', 'Nepherologist'),
    ]

    LANGUAGE = [
        ('English', 'English'),        
        ('Hausa', 'Hausa'),
        ('Igbo', 'Igbo'),
        ('Yoruba', 'Yoruba'),
    ]

    doctor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=30, choices=DOC_SPECIALTY, default='Family Medicine')
    language = models.CharField(max_length=15, choices=LANGUAGE, default='ENGLISH')
    location = models.CharField(max_length=20)
    hospital = models.CharField(max_length=30)
    years_of_experience = models.CharField(max_length=2)
    about = models.TextField()
    
    

    def __str__(self):
        return (
            f'{self.doctor.first_name} {self.doctor.last_name}. '
            f'I am a {self.specialty}, with {self.years_of_experience} years of experince.'
            )
    

class PatientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=TeleMedUser.Role.PATIENT)
    
class Patient(TeleMedUser):
    base_role = TeleMedUser.Role.PATIENT

    patient = PatientManager()

    class Meta:
        proxy = True



class PatientProfile(models.Model):
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('Others',  'Others')
    ]
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=7, choices=GENDER, default='Others')
    alternative_phone = models.CharField(max_length=15, null=True, blank=True)
    emergency_contact_name = models.CharField(max_length=30, null=True, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, null=True, blank=True)
    emergency_contact_relationship = models.CharField(max_length=20, null=True, blank=True)
    medical_plan = models.CharField(max_length=20, null=True, blank=True)
    

    def __str__(self):
        return f'{self.patient.first_name} {self.patient.last_name}'


# Create Doctors and Patients' Profile using their respective models with post_save signal


class DocAvailableDate(models.Model):
    # DAYS_OF_WEEK = [
    #     ('Mon', 'Monday'),
    #     ('Tues', 'Tuesday'),
    #     ('Wed', 'Wednesday'),
    #     ('Thur', 'Thursday'),
    #     ('Fri', 'Friday'),
    #     ('Sat', 'Saturday'),
    #     ('Sun', 'Sunday')
    # ]
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # day1 = models.CharField(max_length=5, choices=DAYS_OF_WEEK)
    from_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    to_time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.from_time} {self.to_time}'
    
    def set_date_time(self):
        pass
